# Synthèse d'activité : france-connect (du 11/05 au 18/05)

## Résumé de l'activité
L'activité récente de FranceConnect s'est concentrée sur l'amélioration de l'expérience utilisateur et de l'accessibilité du support. Des optimisations ont été apportées au tableau de bord, notamment pour une utilisation mobile plus fluide et une meilleure gestion des sessions. L'intégration de nouveaux éléments visuels, comme le logo de l'IdP Yris, et l'ajout de liens de support contextuels sur les pages d'erreur visent à rendre le parcours utilisateur plus intuitif et à faciliter l'assistance en cas de difficulté [sources](/repos/france-connect/sources).

Par ailleurs, l'ouverture de l'eIDASBridge permet désormais de connecter des prestataires de services ayant des exigences de sécurité plus souples, élargissant ainsi les possibilités d'usage du service [sources](/repos/france-connect/sources).

## Sécurité
- Renforcement de l'isolation réseau par la séparation des consommateurs MongoDB selon le niveau d'assurance (faible ou élevé) [sources](/repos/france-connect/sources).
- Amélioration de la protection de la vie privée via la suppression de claims inutilisés ("phone_number" et "address") dans FranceConnect+ [sources](/repos/france-connect/sources).

## Autres changements notables
- Optimisation de la maintenance technique par une refactorisation de la hiérarchie des dossiers pour favoriser le partage de code entre les applications React [sources](/repos/france-connect/sources).
- Amélioration de la traçabilité et du diagnostic grâce à l'implémentation de logs métier détaillés (incluant l'IP et le port client) sur le tableau de bord et FranceConnect+ [sources](/repos/france-connect/sources).
- Renforcement de la fiabilité du système par l'ajout de tests BDD (Behavior Driven Development) sur les notifications et l'historique de connexion [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Évolutions centrées sur l'expérience utilisateur, la sécurité des données et la robustesse de l'infrastructure.
