# Proxy du site institutionnel 2025

Les fichiers de politique (email, sécurité, …) du domaine inclusion.gouv.fr
doivent vivre à la racine du domaine, dans un dossier `.well-known`.

Ce _buildpack_ et la configuration associée permettent de servir les fichiers
statiques directement, et de transmettre les autre requêtes au [_CMS_
sites-faciles de la
plateforme](https://github.com/gip-inclusion/site-institutionnel-2025).
