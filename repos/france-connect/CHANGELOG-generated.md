# Synthèse d'activité : france-connect (du 30/04 au 18/05/2026)

## Résumé de l'activité
L'activité récente de france-connect s'est concentrée sur l'amélioration de l'expérience utilisateur, notamment sur le tableau de bord utilisateur, et sur le renforcement de la sécurité. Des améliorations ont été apportées pour faciliter le support utilisateur avec l'ajout d'un lien vers un formulaire d'assistance sur les pages d'erreur.  Des évolutions techniques ont également été menées pour optimiser l'infrastructure et la maintenabilité du code, notamment avec une meilleure isolation réseau des bases de données MongoDB et un refactoring de l'architecture React.

## Sécurité
- Possibilité de connecter des prestataires de services ayant des exigences de sécurité plus faibles via l'eIDASBridge. [sources](/repos/france-connect/sources)

## Autres changements notables
- Refactorisation de la hiérarchie des dossiers pour améliorer le partage de code entre les applications React. [sources](/repos/france-connect/sources)
- Séparation des consommateurs MongoDB par plateforme pour une meilleure isolation réseau. [sources](/repos/france-connect/sources)
- Ajout de logs métier pour faciliter le suivi et le débogage. [sources](/repos/france-connect/sources)
- Suppression des claims inutilisés "phone_number" et "address" dans FranceConnect+. [sources](/repos/france-connect/sources)

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Amélioration de l'expérience utilisateur, refactoring technique et renforcement de la sécurité.
