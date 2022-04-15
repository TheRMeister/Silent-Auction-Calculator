from solution import find_highest_bidder

# we should add more test to make sure all edge cases are accounted for

# example test if no bids exists
def test_empty(capfd):
    bids = {}
    find_highest_bidder(bids)
    # capturing stdout and stderr
    out, err = capfd.readouterr()

    # what should happen if no name or bid exists?
    assert out == "No bidders"

 
def test_finds_highest_bidder(capfd):
    bids = {
        "bob": 500,
        "tom": 10
    }
    find_highest_bidder(bids)
    # capturing stdout and stderr
    out, err = capfd.readouterr()

    # what should happen if no name or bid exists?
    assert out == "The winner is bob with a bid of $500\n"