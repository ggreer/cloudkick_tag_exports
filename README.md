# To use #

Edit `gen_tag_exports.py` to have a valid Cloudkick OAuth key and secret.

Run...

`./gen_tag_exports.py > blah
source blah`

Once you've sourced the file, you can create scripts like this...

`for i in $TAG_BLAH
do
    ssh $i hostname
done`

...which will run `hostname` on all your servers tagged "blah".