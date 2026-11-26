plugins {
    kotlin("jvm") version "2.4.21"
}
repositories { mavenCentral() }
dependencies { testImplementation("junit:junit:4.13.2") }
kotlin { jvmToolchain(17) }
tasks.test { useJUnit() }
