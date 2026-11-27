plugins {
    kotlin("jvm") version "2.4.21"
    `maven-publish`
}
repositories { mavenCentral() }
dependencies { testImplementation("junit:junit:4.13.2") }
kotlin { jvmToolchain(17) }
tasks.test { useJUnit() }

group = "org.matpomgit"
version = "0.1.0"
publishing {
    publications {
        create<MavenPublication>("mavenJava") { from(components["java"]) }
    }
    repositories { maven { name = "build"; url = uri(layout.buildDirectory.dir("repository")) } }
}
