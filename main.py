proposal = Hash()
ids = Variable()

@construct
def seed():
    proposal['voteCount'] = 0
    ids.set(0)

@export
def createProposal(name: str, proposalVote: str):
    #ID 
    int_id = ids.get() + 1
    ids.set(int_id)

    # CONTRUCTOR PROPOSALS
    proposal['id'] = int_id
    proposal['name'] = name
    proposal['proposal'] = proposalVote
    proposal['votes'] = 0
    proposal['creator'] = ctx.caller

    # TEXT
    nombre = proposal['name'] = name
    proposal_id = proposal['id']
    proposal_pro = proposal['proposal']
    votes = proposal['votes']
    creator = proposal['creator']
    result = [proposal_id, nombre, proposal_pro, votes, creator]
    return result






    
