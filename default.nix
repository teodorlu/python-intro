with import <nixpkgs> {}; {
  pandocEnv = stdenv.mkDerivation {
    name = "pandoc";
    buildInputs = [ stdenv pandoc ];
  };
}
