# Synthèse d'activité : france-connect (du 11/05 au 18/05)

## Résumé de l'activité
L'activité récente s'est concentrée sur l'amélioration de l'expérience utilisateur et l'élargissement des capacités de connexion. Les utilisateurs bénéficieront d'un tableau de bord plus fluide, notamment sur mobile, et d'un meilleur accompagnement en cas d'erreur grâce à l'ajout de liens de support contextuels. Par ailleurs, l'intégration de l'eIDASBridge permet d'ouvrir le service à des prestataires ayant des exigences de sécurité spécifiques, tandis que l'interface prépare déjà l'arrivée de nouveaux identifiants comme l'IdP Yris [sources](/repos/france-connect/sources).

## Sécurité
- Renforcement de l'isolation réseau par la séparation des consommateurs de données MongoDB selon le niveau d'assurance [sources](/repos/france-connect/sources).
- Amélioration de la traçabilité et du diagnostic grâce à l'ajout de logs métier détaillés, incluant désormais la source IP et le port du client [sources](/repos/france-connect/sources).
- Optimisation de la protection des données par la suppression de champs d'information inutilisés (claims "phone_number" et "address") dans FranceConnect+ [sources](/repos/france-connect/sources).

## Autres changements notables
- Refactorisation de l'architecture du code pour faciliter le partage de composants entre les différentes applications React [sources](/repos/france-connect/sources).
- Préparation du futur tableau de bord partenaire via une réorganisation structurelle des composants dédiés aux prestataires de services [sources](/repos/france-connect/sources).
- Renforcement de la qualité logicielle par l'ajout de tests de comportement (BDD) sur les notifications de préférences et l'historique de connexion [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Travaux sur l'interface utilisateur, la sécurité des données et la préparation des évolutions structurelles (partenaires et nouveaux IdP).
