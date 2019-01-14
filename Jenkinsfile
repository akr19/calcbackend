stage("Checkout") {
    node {
      sh "pwd; ls -alsh"
      sh 'rm -rf calcbackend; git clone https://github.com/akr19/calcbackend.git'
      sh "pwd; ls -lash"
      dir('calcbackend') {
          sh "pwd; ls -lash; whoami"
      }
    }
    
}

stage("Build") {
    echo "jest stage build"
}
