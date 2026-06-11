## Changelog : anssi-portail (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'intégration du Design System de la République Française (DSFR) sur de nombreuses pages du portail. Des fonctionnalités importantes ont été ajoutées au parcours sécurisation, permettant aux utilisateurs de prendre en compte les mesures de sécurité et de suivre leur progression. Des corrections de sécurité et des optimisations diverses ont également été apportées.

### Évolutions fonctionnelles
- Intégration du Design System de la République Française (DSFR) sur de nombreuses pages : accueil, services, parcours, catalogue, contacts, etc. pour une interface plus cohérente et accessible.
- Ajout de la possibilité pour les utilisateurs de "prendre en compte" une mesure de sécurité dans le parcours sécurisation.
- Affichage de l'état "pris en compte" des mesures de sécurité.
- Affichage de la progression de l'utilisateur dans le parcours sécurisation.
- Ajout du titre des mesures de sécurité.
- Limitation de la possibilité de donner son avis sur les mesures en mode connecté.
- Ajout d'un encart "tutoriel" pour les mesures.
- Affichage des actions prioritaires et des liens pour aller plus loin sur les mesures.
- Amélioration de la page 404.
- Ajout de la gestion des COT (Contact de Territoire) pour les régions PACA, ARA et Normandie.
- Ajout de la fonctionnalité de soumission et de stockage des avis utilisateurs sur les mesures.

### Évolutions techniques
- Refonte de l'architecture pour supporter la prise en compte des mesures de sécurité.
- Création d'une API pour la liste des mesures de sécurité.
- Utilisation de bannières pour l'affichage d'informations importantes.
- Amélioration de la robustesse des flux et gestion des erreurs.
- Mise à jour de plusieurs dépendances pour des raisons de sécurité et de performance (ruby, svelte, qs, brace-expansion, devalue, fast-xml-builder).
- Fixe la version de node à l'étape du déploiement pour plus de stabilité.
- Amélioration de la gestion des erreurs et des logs.
- Factorisation et simplification du code.
- Suppression de code obsolète.
- Correction d'une vulnérabilité.

### Autres changements
- Documentation mise à jour.
- Suppression de styles CSS inutilisés.
- Amélioration des messages d'erreur.
- Renommage de fichiers et composants pour une meilleure organisation.
- Corrections de typos et d'erreurs de présentation.
- Suppression de jobs d'approbation inutiles.
- Ajout de tests unitaires.
- Amélioration de la configuration CI/CD.
