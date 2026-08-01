## Changelog : france-chaleur-urbaine (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'application, notamment autour de la gestion des demandes de raccordement, de l'intégration de nouvelles données (BRGM, Batenr) et de l'expérience utilisateur. Des efforts ont également été faits pour améliorer la robustesse de l'application et faciliter la maintenance.

### Évolutions fonctionnelles
- Ajout d'un champ commentaire pour les demandes de raccordement, permettant aux utilisateurs de fournir des informations complémentaires.
- Possibilité d'étiqueter les utilisateurs pour une meilleure organisation et gestion des accès.
- Amélioration de l'affichage et de l'ergonomie de la page de résultat du simulateur de chaleur renouvelable, avec ajout d'informations et d'appels à l'action plus clairs.
- Ajout d'un CTA vers France Chaleur Renouvelable sur la carte lorsque l'adresse n'est pas éligible au réseau de chaleur.
- Gestion des alertes pour les demandes non recontactées, permettant une meilleure réactivité.
- Amélioration de la gestion des statuts FCR et de la documentation associée.
- Possibilité de filtrer les données dans les tableaux de conversion.
- Ajout de la gestion du maitre d'ouvrage pour les réseaux en construction.
- Ajout d'une fonctionnalité permettant aux administrateurs de mettre à jour le statut des demandes.
- Amélioration de l'affichage des boutons de modification/suppression pour les relances.
- Ajout de la gestion des abus pour les statistiques.
- Amélioration de la gestion des adresses et correction de bugs liés à l'affichage de la carte.
- Ajout de la gestion des prérequis et des raisons d'inéligibilité pour le simulateur de chaleur renouvelable.

### Évolutions techniques
- Migration de 13 formulaires vers le module formulaire TanStack pour une meilleure gestion et une plus grande cohérence.
- Refactoring et simplification de la page API gestionnaires.
- Utilisation des règles Publicodes v2 pour une meilleure gestion des règles de calcul.
- Amélioration du typage TypeScript pour Publicodes.
- Mise à jour du package Publicodes.
- Centralisation de l'email de contact pour FCR.
- Amélioration de la gestion des erreurs Airtable.
- Correction de problèmes de rendu SSR pour les pages légales et de confidentialité.
- Mise en place de tests Playwright et Cypress pour une meilleure couverture des tests.
- Amélioration de la configuration et du déploiement de l'application.
- Ajout de tests pour les fiches réseau.
- Migration de la table `demands_chaleur_renouvelable`.
- Utilisation de Dialog au lieu de Modal.
- Amélioration de la gestion des migrations de la base de données.

### Autres changements
- Documentation de la procédure de développement en local avec Publicodes.
- Mise à jour de la documentation métier de l'admin et du registre des règles de gestion.
- Suppression de code inutilisé et nettoyage du code.
- Mise à jour des dépendances.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de commentaires et de documentation pour faciliter la maintenance.
- Amélioration de la gestion des logs et des erreurs.
- Ajout de tests unitaires et d'intégration.
- Correction de problèmes de linting.
- Regénération de l'index de documentation.
