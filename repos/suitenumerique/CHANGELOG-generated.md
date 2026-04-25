# Synthèse d'activité : suitenumerique (du 17/04 au 24/04/2026)

## Résumé de l'activité
L'organisation suitenumerique a connu une semaine riche en développement et améliorations sur ses différents projets. L'accent a été mis sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de nouvelles fonctionnalités dans [dictaphone](/repos/suitenumerique/dictaphone), [st-home](/repos/suitenumerique/st-home), [messages](/repos/suitenumerique/messages) et [meet](/repos/suitenumerique/meet). La sécurité a également été renforcée dans plusieurs dépôts, notamment [messages](/repos/suitenumerique/messages) et [people](/repos/suitenumerique/people). De nouveaux projets ont vu le jour, comme [meet-matting](/repos/suitenumerique/meet-matting), et des bases solides ont été posées pour des développements futurs, comme avec le [gallene-sdk](/repos/suitenumerique/gallene-sdk).

## Sécurité
Plusieurs améliorations de sécurité ont été apportées :

- [messages](/repos/suitenumerique/messages) : Renforcement de la sécurité DNS avec validation du temps d'envoi et vérification SPF récursive, factorisation du code SSRF et autorisation des redirections dans le proxy d'image.
- [people](/repos/suitenumerique/people) : Passage à l'envoi de liens de connexion au lieu des mots de passe, correction d'une potentielle escalade de privilèges lors de l'invitation d'utilisateurs et mise à jour de bibliothèques avec des correctifs de sécurité.

## Autres changements notables
- [st-home](/repos/suitenumerique/st-home) : Remplacement de Nginx par Caddy comme reverse proxy pour améliorer la performance et la simplicité de configuration.
- [menshen](/repos/suitenumerique/menshen) : Refonte de la structure des applications en préparation de l'implémentation de l'échange de jetons OAuth 2.0.
- [cunningham](/repos/suitenumerique/cunningham) : Migration de l'infrastructure CI/CD vers GitHub Actions.
- [gallene-deployment](/repos/suitenumerique/gallene-deployment) : Refonte majeure avec l'ajout d'un Dockerfile et de scripts de déploiement basés sur `deburau/galene-docker`.
- [ui-kit](/repos/suitenumerique/ui-kit) : Automatisation de la génération des icônes SVG à partir de Figma.
- [conversations](/repos/suitenumerique/conversations) : Mise à jour de Next.js de la version 15 à la version 16.

## Dépôts les plus actifs
- [dictaphone](/repos/suitenumerique/dictaphone) : Ajout de nouvelles fonctionnalités pour la transcription audio et la gestion des enregistrements.
- [st-home](/repos/suitenumerique/st-home) : Amélioration de la carte de déploiement et ajout d'une page dédiée aux partenaires OPSN.
- [messages](/repos/suitenumerique/messages) : Ajout de fonctionnalités de messagerie interne et d'amélioration de la sécurité.
- [meet](/repos/suitenumerique/meet) : Amélioration du partage de documents et de la gestion des tâches de transcription.
- [ui-kit](/repos/suitenumerique/ui-kit) : Amélioration de la bibliothèque de composants UI avec de nouvelles fonctionnalités et corrections de bugs.
- [people](/repos/suitenumerique/people) : Amélioration de la sécurité et de l'expérience utilisateur pour la gestion des utilisateurs.
