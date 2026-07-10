## Changelog : mon-indemnisation-justice (30 derniers jours, au 06 juillet 2026)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives en termes de gestion des données (import CSV, entités FDO), de correction de bugs (affichage, PDF, erreurs FIP6/FDO) et d'expérience utilisateur (navigation, affichage des pièces jointes, onglets agents). Un nouveau module de test d'éligibilité a été développé pour l'espace public. Des travaux ont également été réalisés pour améliorer la robustesse et la fiabilité de l'application, notamment au niveau du worker et de la gestion des erreurs.

### Évolutions fonctionnelles
- Ajout d'un importeur CSV basique pour les données des gendarmeries.
- Création d'un nouvel onglet "Agents à valider" pour faciliter la gestion des agents.
- Amélioration de la navigation et de l'affichage des listes d'agents (séparation actifs/inactifs en onglets).
- Possibilité de modifier les critères de recherche des dossiers.
- Affichage des pièces jointes au format PDF directement dans l'application.
- Intégration du test d'éligibilité pour les dysfonctionnements dans l'espace public.
- Mise à jour de l'avis d'intervention pour la Gendarmerie Nationale.
- Amélioration du navigateur de pages avec correction de glitchs d'affichage.
- Ajout d'une frise temporelle pour l'historique des dossiers.
- Suppression de la quittance subrogative pour les bailleurs sociaux.

### Évolutions techniques
- Intégration de `vite-plugin-node-polyfills` pour résoudre les erreurs de conversion Node -> Browser.
- Refonte de l'architecture du worker avec l'utilisation de `pierrelemee/supervisor-docker` pour la gestion des tâches cron.
- Déploiement des applications web et worker sur l'environnement `develop`.
- Correction de l'utilisation de `vite-plugin-static-copy` en dépendance non dev.
- Utilisation de l'URL de déconnexion fournie par l'API pour une meilleure gestion de la déconnexion.
- Amélioration de la gestion des erreurs FIP6 et FDO avec affichage et remontée des erreurs.
- Refactoring de l'espace public avec amélioration de la qualité et de la cohérence du code.
- Utilisation de la version legacy de `react-pdf` pour résoudre des problèmes de compatibilité.
- Injection de l'URL de déconnexion dans le contexte agent.

### Autres changements
- Correction du bouton du SideMenu pour empêcher la soumission du formulaire.
- Intégration de la FAQ modifiée.
- Figeage de la configuration de supervisor dans le Dockerfile du worker.
- Ajout d'un test unitaire sur la route de suppression.
- Création d'une modale de suppression de pièce jointe (sans action réelle pour le moment).
- Correction de l'adresse pouvant être manquante sur un dossier.
- Correction de bugs liés à la modale de mot de passe oublié.
- Fluidification de l'affichage des champs en tiroir.
- Purge de la boîte de réception et envoi des emails au chargement des fixtures.
- Correction d'un argument optionnel dans `Requerant.nomSimple`.
- Correction de tests unitaires.
- Provisionnement des données en test et en production.
- Intégration du Ministère de l'intérieur comme administration.
- Ajout de modèles TypeScript et de conteneurs Inversify pour le TestEligibiliteManager.
- Suppression de Storybook sur l'espace visiteur et mise en place d'un routeur.
- Ajout de formulaires Tanstack sur les pages de l'espace public.
- Refactoring du code pour améliorer la qualité et la cohérence.
