package pl.edu.prz.arcadhd.audio

import org.junit.Assert.assertArrayEquals
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class EngineeringStereoSignalTest {
    private val signal = EngineeringStereoSignal()

    @Test
    fun chunksMatchOneContinuousRenderAcrossChannelChanges() {
        val count = signal.framesPerSide * 2 + 33
        val whole = FloatArray(count * 2)
        // Work in bounded chunks, as required by the renderer.
        var offset = 0
        while (offset < count) {
            val frames = minOf(EngineeringStereoSignal.MAX_BUFFER_FRAMES, count - offset)
            signal.render(StereoCondition.ALTERNATING, offset.toLong(), frames)
                .copyInto(whole, offset * 2)
            offset += frames
        }
        val other = FloatArray(count * 2)
        offset = 0
        while (offset < count) {
            val frames = minOf(127, count - offset)
            signal.render(StereoCondition.ALTERNATING, offset.toLong(), frames)
                .copyInto(other, offset * 2)
            offset += frames
        }
        assertArrayEquals(whole, other, 0f)
    }

    @Test
    fun alternatingChannelsAndStartingSideAreDeterministic() {
        val first = signal.render(StereoCondition.ALTERNATING, 25L, 1)
        val second = signal.render(StereoCondition.ALTERNATING, signal.framesPerSide + 25L, 1)
        val rightFirst = signal.render(StereoCondition.ALTERNATING, 25L, 1, FirstChannel.RIGHT)
        assertTrue(kotlin.math.abs(first[0]) > 0f)
        assertEquals(0f, first[1], 0f)
        assertEquals(0f, second[0], 0f)
        assertEquals(0f, rightFirst[0], 0f)
        assertEquals(first[0], rightFirst[1], 0f)
    }

    @Test
    fun matchedAndAlternatingHaveEqualSampleWiseSummedDigitalEnergy() {
        val starts = listOf(25L, signal.framesPerSide - 1L, signal.framesPerSide.toLong(),
            signal.framesPerSide + 25L, 2L * signal.framesPerSide - 100L)
        for (frame in starts) {
            val a = signal.render(StereoCondition.ALTERNATING, frame, 1)
            val b = signal.render(StereoCondition.MATCHED_STEREO, frame, 1)
            val energyA = a[0] * a[0] + a[1] * a[1]
            val energyB = b[0] * b[0] + b[1] * b[1]
            assertEquals(energyB, energyA, 1e-7f)
            assertEquals(b[0], b[1], 0f)
        }
    }

    @Test
    fun quietAlwaysProducesZeros() {
        assertTrue(signal.render(StereoCondition.QUIET, 12345, 4096).all { it == 0f })
    }

    @Test
    fun rejectsUnboundedBuffersAndInvalidConfiguration() {
        assertFails { signal.render(StereoCondition.ALTERNATING, -1, 1) }
        assertFails { signal.render(StereoCondition.ALTERNATING, 0, 4097) }
        assertFails { signal.render(StereoCondition.ALTERNATING, Long.MAX_VALUE, 2) }
        assertFails { StereoSignalConfig(peakAmplitude = Double.NaN) }
        assertFails { StereoSignalConfig(peakAmplitude = 0.3) }
        assertFails { StereoSignalConfig(crossfadeMs = 250) }
    }

    private fun assertFails(block: () -> Unit) {
        try {
            block()
        } catch (_: IllegalArgumentException) {
            return
        }
        throw AssertionError("Expected IllegalArgumentException")
    }
}
