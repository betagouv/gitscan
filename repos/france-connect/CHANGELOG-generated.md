# Synthèse d'activité : france-connect (du 11/05 au 18/05)

## Résumé de l'activité
L'activité récente de FranceConnect s'est concentrée sur l'amélioration de l'expérience utilisateur et l'élargissement des capacités de connexion. Des optimisations ont été apportées au tableau de bord, notamment pour une utilisation mobile plus fluide et une meilleure gestion des sessions, ainsi que l'ajout de liens de support pour faciliter l'assistance en cas d'erreur. Par ailleurs, l'intégration de l'eIDASBridge permet désormais de connecter des prestataires ayant des exigences de sécurité spécifiques [sources](/repos/france-connect/sources).

## Sécurité
- Renforcement de l'isolation réseau par la séparation des consommateurs MongoDB selon le niveau d'assurance [sources](/repos/france-connect/sources).
- Amélioration de la protection des données par la suppression de claims inutilisés ("phone_number" et "address") dans FranceConnect+ [sources](/repos/france-connect/sources).
- Amélioration de la traçabilité et du diagnostic grâce à l'ajout de logs métier détaillés, incluant l'adresse IP et le port client [sources](/repos/france-connect/sources).

## Autres changements notables
- Refactorisation de la structure des dossiers pour améliorer le partage de code entre les différentes applications React [sources](/repos/france-connect/sources).
- Optimisation des performances via l'ajout de contrôles de cache sur les routes de métadonnées [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Évolutions de l'interface utilisateur, renforcement de la sécurité et refactorisation technique.
