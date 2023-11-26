# 1-install _a_package.pp
# Installs Flask using pip3

package { 'Flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
