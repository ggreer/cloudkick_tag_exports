# WTF Does this thing do? #

This script grabs your list of nodes from the Cloudkick API and outputs an easily-sourced file. This is super handy for running a script on all of your servers with a given tag.

# To use #

Edit `gen_tag_exports.py` to have a valid Cloudkick OAuth key and secret.

Run...

    ./gen_tag_exports.py > blah

The file blah should look something like this:

    export TAG_EXAMPLE1="10.0.0.1"
    export TAG_EXAMPLE2="10.0.0.1 10.0.0.3"
    export TAG_TEST="10.0.0.1 10.0.0.2"

Once you've sourced the file (`source blah`), you can create scripts like this...

    for i in $TAG_TEST
    do
        ssh $i hostname
    done

...which will run `hostname` on all your servers tagged "test".

# Caveats #

Tag names are mangled so that they're valid in shell-land. Spaces are replaced with underscores. I'm sure some people will have crazy symbols in their tags that will break this script.