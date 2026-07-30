## Changelog : france-chaleur-urbaine (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'administration de l'outil, notamment la gestion des utilisateurs, des demandes et des données. L'intégration du simulateur de PAC a été finalisée et des améliorations significatives ont été apportées à la cartographie et à l'expérience utilisateur, en particulier pour les demandes de chaleur renouvelable.

### Évolutions fonctionnelles
- Ajout de la possibilité de filtrer globalement les colonnes dans les tableaux de conversion.
- Amélioration de l'affichage des boutons de modification/suppression pour les relances.
- Possibilité pour les administrateurs de mettre à jour le statut des demandes.
- Ajout du maître d'ouvrage aux réseaux en construction.
- Gestion des abus pour les statistiques.
- Ajout de commentaires utilisateurs sur les demandes de raccordement.
- Implémentation d'alertes pour les demandes non recontactées.
- Ajout d'un CTA vers France Chaleur Renouvelable sur la carte lorsque l'adresse n'est pas éligible.
- Amélioration de l'affichage et de l'ergonomie du comparateur de PAC.
- Ajout d'un champ commentaire sur les demandes de chaleur renouvelable.
- Ajout d'un champ type de radiateur sur la landing page.
- Gestion des étiquettes utilisateurs (tags) pour faciliter l'organisation et le suivi.
- Amélioration de la gestion des erreurs et des messages d'information.
- Ajout de la possibilité de supprimer en masse des demandes.
- Ajout d'un champ pour la gestion des organisations.
- Affichage des accès aux demandes sur une seule ligne.

### Évolutions techniques
- Migration vers le module formulaire TanStack pour 13 formulaires, améliorant la performance et la maintenabilité.
- Utilisation des règles Publicodes v2 pour une gestion plus flexible et efficace des règles de calcul.
- Refactorisation de l'API PAC pour une meilleure organisation et maintenabilité.
- Mise à jour du package Publicodes.
- Amélioration de la gestion des cookies pour les grandes tailles.
- Centralisation de l'email de contact pour FCR.
- Centralisation des statuts de FCR dans la documentation.
- Configuration des tests Playwright et PostgreSQL.
- Amélioration du typage TypeScript pour Publicodes.
- Utilisation de Dialog et ConfirmDialog pour une meilleure expérience utilisateur.
- Suppression de code obsolète et nettoyage du code.
- Amélioration de la gestion des migrations de base de données.
- Ajout de tests unitaires et d'intégration.
- Optimisation des performances de l'application.

### Autres changements
- Documentation de la procédure de développement en local avec Publicodes.
- Mise à jour de la documentation métier et du registre des règles de gestion FCR.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour des dépendances.
- Amélioration de la gestion des erreurs Airtable.
- Correction de problèmes de rendu SSR pour les pages légales et de confidentialité.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Amélioration de la gestion des événements et du tracking.
- Mise à jour des données des études en cours.
- Correction de problèmes de compatibilité avec les anciennes iframes.
- Amélioration de la gestion de l'imposture administrateur.
- Ajout d'un lien vers le formulaire de contact depuis mes demandes.
