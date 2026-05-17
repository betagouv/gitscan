## Changelog : reva (30 derniers jours, au 17 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment autour de la gestion des lieux d'accueil et des candidatures. Des corrections de bugs et des optimisations de sécurité ont également été apportées, ainsi que des améliorations techniques pour faciliter le développement et la maintenance du projet. L'authentification via FranceConnect a été renforcée et des outils de nettoyage ont été ajoutés pour faciliter la gestion des données de test.

### Évolutions fonctionnelles
- Ajout d'une page squelette pour la gestion des informations de contact des organismes certificateurs [#f849ff2](https://github.com/betagouv/reva/pulls/f849ff2).
- Possibilité de cliquer sur la tuile d'un organisme certificateur pour accéder à sa page d'informations de contact [#7f3b226](https://github.com/betagouv/reva/pulls/7f3b226).
- Suppression des détails de contact du tableau de bord des contacts [#632f698](https://github.com/betagouv/reva/pulls/632f698).
- Amélioration de la formulation dans l'administration, pour les candidats et pour les VAE collectives [#4dfc681](https://github.com/betagouv/reva/pulls/4dfc681).
- Possibilité de réinitialiser une candidature si le candidat confirme la fin de l'accompagnement [#0c67f10](https://github.com/betagouv/reva/pulls/0c67f10).
- Ajout d'une page de détails des résultats de jury pour les candidats [#b109b26](https://github.com/betagouv/reva/pulls/b109b26).
- Amélioration de la lisibilité de la page de fin d'accompagnement en mode lecture seule [#afeb702](https://github.com/betagouv/reva/pulls/afeb702).
- Ajout d'un bouton de suppression pour les lieux d'accueil dans la page de détails, avec une confirmation pour éviter les suppressions accidentelles [#bdb1342](https://github.com/betagouv/reva/pulls/bdb1342).
- Ajout d'un avertissement lors de la suppression d'un lieu d'accueil ayant des candidatures associées [#bd214c5](https://github.com/betagouv/reva/pulls/bd214c5).
- Possibilité de supprimer une candidature en tant que certificateur, même si elle a été confirmée par le candidat [#5f9bdb2](https://github.com/betagouv/reva/pulls/5f9bdb2).
- Ajout d'une page d'archivage des candidatures et d'une fonctionnalité d'archivage correspondante [#331c34b](https://github.com/betagouv/reva/pulls/331c34b).
- Ajout d'un bouton de suppression de candidature si le statut est "PROJET" [#6294271](https://github.com/betagouv/reva/pulls/6294271).
- Amélioration de la page de gestion des dates de jury dans l'administration [#32977a0](https://github.com/betagouv/reva/pulls/32977a0).
- Ajout d'une page de résultats par blocs pour les AAP [#9488e6e](https://github.com/betagouv/reva/pulls/9488e6e).

### Évolutions techniques
- Refactorisation de l'authentification dans l'administration pour utiliser des cookies et améliorer la sécurité [#86d59df](https://github.com/betagouv/reva/pulls/86d59df).
- Mise à jour de Next.js dans plusieurs packages (admin, candidate, vae-collective, website) [#c2e0cfb](https://github.com/betagouv/reva/pulls/c2e0cfb), [#93981f6](https://github.com/betagouv/reva/pulls/93981f6), [#31293dd](https://github.com/betagouv/reva/pulls/31293dd), [#725e92c](https://github.com/betagouv/reva/pulls/725e92c).
- Amélioration de la gestion des tokens et des cookies pour une meilleure sécurité et une meilleure expérience utilisateur [#7c7b3cc](https://github.com/betagouv/reva/pulls/7c7b3cc), [#e9c7698](https://github.com/betagouv/reva/pulls/e9c7698), [#9c17500](https://github.com/betagouv/reva/pulls/9c17500).
- Ajout de scripts pour anonymiser les bases de données Reva et Keycloak [#0061807](https://github.com/betagouv/reva/pulls/0061807).
- Amélioration de la gestion des logs pour les suppressions de lieux d'accueil [#dc5971f](https://github.com/betagouv/reva/pulls/dc5971f).
- Mise à jour des dépendances (axios, uuid, fastify, etc.) dans divers packages.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Suppression des logs de traçage de l'usurpation d'identité dans l'administration [#7c817ab](https://github.com/betagouv/reva/pulls/7c817ab).
- Correction d'un problème avec l'attribut Domain du cookie d'usurpation d'identité [#6f6b2f2](https://github.com/betagouv/reva/pulls/6f6b2f2).
- Correction d'un bug empêchant l'usurpation d'identité de fonctionner avec tous les rôles [#ce7041d](https://github.com/betagouv/reva/pulls/ce7041d).
- Correction d'un problème d'hydratation de la carte de fin d'accompagnement [#7b14051](https://github.com/betagouv/reva/pulls/7b14051).
- Ajout de tests pour la fonctionnalité de fin d'accompagnement [#3ce0de2](https://github.com/betagouv/reva/pulls/3ce0de2).
- Amélioration de la configuration de Strapi pour le déploiement en cloud [#db8f98d](https://github.com/betagouv/reva/pulls/db8f98d).
- Mise à jour de la configuration de Keycloak pour supporter la version 26.6.1 [#ddbf57a](https://github.com/betagouv/reva/pulls/ddbf57a).
- Augmentation légère de la limite de débit d'interopérabilité Traefik [#f3bf3eb](https://github.com/betagouv/reva/pulls/f3bf3eb).
- Ajout de margin sur le bouton de suppression d'un lieu d'accueil [#fc63b38](https://github.com/betagouv/reva/pulls/fc63b38).
- Ajout d'un resolver `organism->hasCandidacies` [#cad5995](https://github.com/betagouv/reva/pulls/cad5995).
- Prévention de la fin d'accompagnement si la faisabilité de la candidature est en attente [#e8d953b](https://github.com/betagouv/reva/pulls/e8d953b).
- Ajout de tests pour la nouvelle page de détails des résultats de jury [#5eb9f4b](https://github.com/betagouv/reva/pulls/5eb9f4b).
- Amélioration de la formulation du modal de confirmation de fin d'accompagnement [#63d6963](https://github.com/betagouv/reva/pulls/63d6963).
- Ajout d'une protection contre les attaques de type "confused deputy" dans l'interop [#0078369](https://github.com/betagouv/reva/pulls/0078369).
- Amélioration de la sécurité de la vérification des JWT [#a077cbd](https://github.com/betagouv/reva/pulls/a077cbd).
- Suppression de code obsolète et nettoyage du code.
