## Changelog : territoires-en-transitions (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur autour des audits et des référentiels, avec une refonte de l'interface de gestion des audits, l'ajout de nouvelles fonctionnalités pour la gestion des preuves et des documents, et des optimisations de performance.  Des travaux importants ont également été réalisés pour préparer l'import de plans d'action via l'IA, avec la mise en place de l'infrastructure nécessaire à l'extraction et au traitement des données.

### Évolutions fonctionnelles

*   **Audits et Labellisation :**
    *   Possibilité pour un super-admin en mode support de déposer des preuves. [#1234](https://github.com/incubateur-ademe/territoires-en-transitions/issues/1234)
    *   L'auditeur peut remplacer le rapport d'audit.
    *   Amélioration de l'interface de gestion des audits avec une nouvelle checklist, une meilleure organisation des informations et la possibilité de gérer les documents directement depuis l'interface.
    *   Affichage du conseiller référent dans le header de la checklist d'audit.
    *   Possibilité de télécharger une archive des preuves d'un audit.
    *   Clôture d'un audit en deux étapes avec une modale de confirmation.
    *   Affichage d'un badge de statut d'audit sur l'onglet.
    *   Les preuves de mesures sont maintenant limitées à la fenêtre de l'audit.
*   **Plans et Actions :**
    *   Ajout d'une action "Dupliquer le plan" avec une modale de saisie du nom.
    *   Copie des budgets détaillés lors de la duplication d'un plan.
    *   Possibilité de dupliquer une action depuis son identifiant.
*   **Référentiels :**
    *   Liste des archives de preuves avec affichage de la validité.
    *   Possibilité de masquer les colonnes d'audit dans la vue tabulaire.
    *   Amélioration de l'affichage des informations de la mesure.
    *   Les preuves de labellisation sont verrouillées une fois l'audit validé.
*   **Interface Utilisateur :**
    *   Amélioration de l'accessibilité et de la navigation avec l'ajout d'un autofocus sur les champs de recherche.
    *   Utilisation d'un nouveau composant `FloatingPanel` pour les fenêtres modales non-bloquantes.

### Évolutions techniques

*   **Architecture :**
    *   Refactor de l'architecture de l'import de plans d'action via l'IA avec création de nouveaux services et repositories.
    *   Migration de l'authentification vers une application Next.js unique.
    *   Suppression de l'utilisation de vues publiques `crm_*` dans la base de données.
*   **Performance :**
    *   Optimisation des performances en différant le chargement des dépendances lourdes.
    *   Parallélisation des tests e2e en CI.
*   **Sécurité :**
    *   Correction de failles de sécurité potentielles (IDOR, SSRF, phishing).
    *   Restriction des accès aux objets de stockage Supabase.
*   **Infrastructure :**
    *   Mise à jour des dépendances (Next.js, eslint-config-next, posthog-js).
    *   Épinglage de la version de Node.js à 24.18.0 pour corriger une régression.
*   **Tests :**
    *   Ajout de tests e2e pour les nouvelles fonctionnalités.
    *   Amélioration de la couverture des tests unitaires.

### Autres changements

*   Documentation mise à jour pour les contournements de configuration de Storybook.
*   Nettoyage du code et suppression de libellés inutilisés.
*   Mise à jour du schéma des préférences de la collectivité.
*   Amélioration de la documentation pour les agents IA.
*   Ajout d'un plan de migration pour les applications d'authentification.
*   Mise à jour des données de test pour le référentiel TE.
*   Amélioration de la synchronisation des données CRM depuis les outils.
*   Correction de bugs mineurs et améliorations de la qualité du code.
