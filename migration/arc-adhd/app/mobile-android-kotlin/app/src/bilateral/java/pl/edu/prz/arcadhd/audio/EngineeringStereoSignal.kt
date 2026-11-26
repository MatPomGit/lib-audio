package pl.edu.prz.arcadhd.audio

import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin
import kotlin.math.sqrt

/** Candidate P03 conditions; no assignment, output routing or playback is implemented here. */
enum class StereoCondition { ALTERNATING, MATCHED_STEREO, QUIET }

enum class FirstChannel { LEFT, RIGHT }

/** Normalized digital levels are not calibrated sound-pressure levels. */
data class StereoSignalConfig(
    val sampleRateHz: Int = 48_000,
    val toneHz: Int = 440,
    val sideDurationMs: Int = 500,
    val crossfadeMs: Int = 5,
    val peakAmplitude: Double = 0.1,
) {
    init {
        require(sampleRateHz in 8_000..96_000)
        require(toneHz in 100..2_000 && toneHz * 2 < sampleRateHz)
        require(sideDurationMs in 200..2_000)
        require(crossfadeMs in 1..sideDurationMs / 4)
        require(peakAmplitude.isFinite() && peakAmplitude > 0.0 && peakAmplitude <= 0.2)
        // Integer frame boundaries avoid cumulative scheduler rounding drift.
        require(sampleRateHz.toLong() * sideDurationMs % 1_000L == 0L)
        require(sampleRateHz.toLong() * crossfadeMs % 1_000L == 0L)
    }
}

/**
 * Pure, deterministic, interleaved stereo Float PCM generator for technical P03 tests.
 *
 * The alternating condition crossfades with constant-power panning. The matched
 * condition sends the same tone simultaneously to both channels at 1/sqrt(2)
 * gain. Their instantaneous summed digital squared amplitudes match, but this
 * does not establish equal acoustic loudness or safe headphone exposure.
 *
 * Rendering is indexed by absolute frame number, so splitting a signal into
 * buffers cannot reset its phase or alternation. An external, independently
 * validated audio driver must handle output, route checks, and immediate stop.
 */
class EngineeringStereoSignal(val config: StereoSignalConfig = StereoSignalConfig()) {
    val framesPerSide: Int = (config.sampleRateHz.toLong() * config.sideDurationMs / 1_000).toInt()
    private val fadeFrames: Int =
        (config.sampleRateHz.toLong() * config.crossfadeMs / 1_000).toInt()

    fun render(
        condition: StereoCondition,
        startFrame: Long,
        frameCount: Int,
        firstChannel: FirstChannel = FirstChannel.LEFT,
    ): FloatArray {
        require(startFrame >= 0L)
        require(frameCount in 0..MAX_BUFFER_FRAMES)
        require(startFrame <= Long.MAX_VALUE - frameCount)
        val samples = FloatArray(frameCount * 2)
        if (condition == StereoCondition.QUIET) return samples

        for (index in 0 until frameCount) {
            val frame = startFrame + index
            val phaseFrame = frame % config.sampleRateHz
            val tone = sin(2.0 * PI * config.toneHz * phaseFrame / config.sampleRateHz) *
                config.peakAmplitude
            val leftGain: Double
            val rightGain: Double
            if (condition == StereoCondition.MATCHED_STEREO) {
                leftGain = MATCHED_CHANNEL_GAIN
                rightGain = MATCHED_CHANNEL_GAIN
            } else {
                val segment = frame / framesPerSide
                val position = (frame % framesPerSide).toInt()
                val leftActive = (segment % 2L == 0L) == (firstChannel == FirstChannel.LEFT)
                val originalGain: Double
                val nextGain: Double
                if (position >= framesPerSide - fadeFrames) {
                    val progress = (position - (framesPerSide - fadeFrames) + 1).toDouble() /
                        fadeFrames
                    originalGain = cos(PI * progress / 2.0)
                    nextGain = sin(PI * progress / 2.0)
                } else {
                    originalGain = 1.0
                    nextGain = 0.0
                }
                leftGain = if (leftActive) originalGain else nextGain
                rightGain = if (leftActive) nextGain else originalGain
            }
            samples[2 * index] = (tone * leftGain).toFloat()
            samples[2 * index + 1] = (tone * rightGain).toFloat()
        }
        return samples
    }

    companion object {
        const val MAX_BUFFER_FRAMES = 4_096
        private val MATCHED_CHANNEL_GAIN = 1.0 / sqrt(2.0)
    }
}
