# Synthèse d'activité : france-connect (du 11/05 au 18/05)

## Résumé de l'activité
L'activité de cette semaine a été ralentie par une période de vacances, mais a permis de faire progresser l'expérience utilisateur, notamment sur le tableau de bord mobile et l'intégration visuelle du futur IdP Yris. Des évolutions ont également été apportées pour faciliter l'assistance technique via de nouveaux liens de support contextuels et pour élargir l'écosystème grâce à l'eIDASBridge [sources](/repos/france-connect/sources).

## Sécurité
- Amélioration de l'isolation réseau par la séparation des consommateurs MongoDB selon le niveau d'assurance [sources](/repos/france-connect/sources).
- Renforcement de la confidentialité des données par la suppression de claims inutilisés ("phone_number" et "address") dans FranceConnect+ [sources](/repos/france-connect/sources).

## Autres changements notables
- Refactorisation de l'architecture des dossiers pour optimiser le partage de code entre les applications React [sources](/repos/france-connect/sources).
- Amélioration de la capacité de diagnostic grâce à l'ajout de logs métier détaillés (incluant l'IP et le port client) [sources](/repos/france-connect/sources).
- Renforcement de la fiabilité logicielle par l'ajout de tests de comportement (BDD) sur les notifications et l'historique de connexion [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Évolutions centrées sur l'expérience utilisateur, la traçabilité et la structure technique du projet.
