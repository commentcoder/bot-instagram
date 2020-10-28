from instapy import InstaPy
from instapy import smart_run

insta_username = 'VOTRE_NOM_D_UTILISATEUR_INSTAGRAM'
insta_password = 'VOTRE_MOT_DE_PASS_INSTAGRAM'
TAGS_A_SUIVRE = []
TAGS_A_EVITER = []
POD = ''

session = InstaPy(
  username=insta_username,
	password=insta_password,
	headless_browser=True)  # Permet de ne pas ouvrir de navigateur et fonctionner de manière invisible

with smart_run(session):
    # Permet de définir quel type de profil vous voulez suivre, s'ils ont beaucoup d'abonnés, quel ratio following/followers etc
    session.set_relationship_bounds(
	    enabled=True,
		delimit_by_numbers=True,
		max_followers=5000,
		min_followers=50,
		min_following=100)

    # Permet de définir les Hashtags à éviter
    session.set_dont_like(TAGS_A_EVITER)

    # On suivra 20% des comptes pour lesquels on vient d'aimer le contenu
    session.set_do_follow(True, percentage=20)

    # Commenter des posts
    session.set_do_comment(enabled=True, percentage=80)

    session.set_comments([
	    u'Ça à l'air bon ! :heart_eyes:',
		u'Super photo ! :wink:',
		u'Magnifique !! :heart_eyes:',
		media='Photo')

    # Préparatifs terminés, on commence l'activité avec les likes
    # L'action d'aimer par tags
    session.like_by_tags(TAGS_A_SUIVRE, amount=2)

    # Se désabonner des comptes Instagram qui ne vous suivent pas en retour
    session.unfollow_users(
	    amount=500,
		nonFollowers=True, # Que des comptes qui ne vous suivent pas en retour
		style='FIFO', # "First In, First Out", on élimine les plus anciens "non-followers" d'abord
		unfollow_after=12 * 60 * 60, # Après 12 heures
		sleep_delay=601) # Pour éviter de trop spammer Instagram

    # Rejoindre un Instagram Pod de nourriture, sans commenter, juste des likes
    session.join_pods(topic=POD, engagement_mode='no_comments')
