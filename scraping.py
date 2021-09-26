from bs4 import BeautifulSoup

html_doc = """

<!DOCTYPE html>
<html>
<head>
    <title>Scraping python</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
	<div id="banner">
		<div class="logo h4 p-3 text-white" >
			<span class="text-left">Ursula</span>
			<span class="fa-pull-right"><a href="register.php" class="text-white">Créer un compte</a></span>
		</div>
	</div>
	<div id="main-container" class="container">
		<div id="main-body">
			<div id="login">	
				<div class="wellcome">
					<div class="h1 text-white">Bienvenue sur Ursula</div>
					<div class="h6 text-white text-center">Connectez vous et accéder au WebLinux</div>
				</div>
				<div id="avatar" class="mt-5 mb-3 text-center">
					<span class="avatar-pic">
						<span>U</span>
					</span>
				</div>
				<div class="mb-4 text-center text-white p-2" id="loader-container"></div>
				<div class="form-login">
					<form id="form" action="identify.php">
						<div class="main-form">
							<input type="text" id="data" name="data" class="form-control gbl-form" placeholder="Matricule/Adresse email"  autocomplete="on"><br>
						</div>
						<div>
							<div class="btn-block btn btn-default btn-sender text-white" style="border-radius: 50px;">
								<span id="launch">Lancer l'identification</span>
								<span id="connect" class="connect">Se connecter</span>
								<span id="new_account">Créer un compte</span>
								<span id="loader"><img src="rsrc/icons/loading-bars.svg" width="30" height="30"></span>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
	<div class="credit mt-5">
		<div class="credit-elm">Dje Bi Jeanmarc</div>
		<div class="credit-elm">Bakayoko Olivia</div>
		<div class="credit-elm">Yao Bini</div>
	</div>
</body>
</html>


"""



soup = BeautifulSoup(html_doc, "html.parser")

#print(soup.body)
#print(soup.head.title)

#   Chercher un élément
#el = soup.find("div")

#   Chercher plusieurs éléments
#el = soup.find_all("div")

#el = soup.find(id="main-body")

#el = soup.find(class_ = "text-center")

#   Navigation
#el = soup.body.contents

#el = soup.body.contents[1].find_next_sibling()


el = soup.find(id="login").find_previous_sibling()


print(el)