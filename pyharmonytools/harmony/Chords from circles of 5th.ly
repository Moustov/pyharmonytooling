% use https://www.hacklily.org/ to display this score

\paper {
  #(set-paper-size "a4")
}

\header {
  title = "Chords from circles of 5th"
  composer = "Moustov"
}

\score {
  \new Staff {
    \clef treble
    \key c \major
    \time 4/4

    \relative c' {
      \mark "Major scale"
      c4^"C" d^"Dm" e^"Em" f^"F" g^"G" a^"Am" b^"Bdim" c
    }
  }
  \layout { }
  \midi { }
}
\score {
  \new Staff {
    \clef treble
    \key c \major
    \time 4/4

    \relative c' {
      \mark "Natural minor scale"
      c4^"Cm" d^"Dm" es^"Eb" f^"F♯maug5" g^"Gm" as^"Ab" bes^"Bb" c
    }
  }
  \layout { }
  \midi { }
}
\score {
  \new Staff {
    \clef treble
    \key c \major
    \time 4/4

    \relative c' {
      \mark "Harmonic Minor scale"
      c4^"Cm" d^"Ddim" es^"Ebaug" f^"Fm" g^"Gadd4" as b^"B-9(no5)" c
    }
  }
  \layout { }
  \midi { }
}
\score {
  \new Staff {
    \clef treble
    \key c \major
    \time 4/4

    \relative c' {
      \mark "Melodic Minor scale (ascending)"
      c4^"Cm" d^"Dm" es^"Ebaug" f^"F5b" g^"Gsus4(no5)" a^"Amsus4(no5)" b^"B-9(no5)" c
    }
  }
  \layout { }
  \midi { }
}