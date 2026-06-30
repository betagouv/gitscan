## Changelog : territoires-en-transitions (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans la gestion des audits et des référentiels, avec une refonte de l'interface de labellisation et l'ajout de nouvelles fonctionnalités comme l'archivage des preuves. Des efforts importants ont également été déployés pour améliorer la sécurité et la performance de la plateforme, notamment en corrigeant des vulnérabilités et en optimisant le chargement des données. L'import de plans via l'IA progresse avec l'ajout de nouveaux extracteurs et une architecture plus robuste.

### Évolutions fonctionnelles
- **Audits et Labellisation :**
    - Nouvelle interface pour la gestion des audits, incluant une vue checklist plus intuitive et la possibilité de remplacer le rapport d'audit par l'auditeur. [#29 juin 2026]
    - Possibilité de masquer les colonnes d'audit dans le référentiel. [#29 juin 2026]
    - Les notes de l'auditeur sont désormais modifiables directement en ligne. [#29 juin 2026]
    - Clôture d'audit en deux étapes avec une modale de confirmation. [#29 juin 2026]
    - Intégration des informations d'audit directement dans la vue tableau du référentiel, supprimant l'onglet "Suivi". [#25 juin 2026]
    - Affichage du conseiller référent dans l'en-tête de la checklist d'audit. [#25 juin 2026]
    - Possibilité de télécharger une archive des preuves d'un audit. [#25 juin 2026]
- **Référentiels :**
    - Ajout d'un endpoint pour lister les archives de preuves, permettant d'accéder aux anciennes versions. [#29 juin 2026]
    - Possibilité d'éditer le conseiller directement depuis l'en-tête du référentiel. [#29 juin 2026]
    - Amélioration de l'affichage des preuves de mesures, limitées à la fenêtre de l'audit. [#16 juin 2026]
    - Les preuves de labellisation sont verrouillées une fois l'audit validé. [#16 juin 2026]
- **Plans d'action :**
    - Ajout d'une action "Dupliquer l'action" dans les menus de fiche. [#10 juin 2026]
    - Copie des budgets détaillés et des preuves/documents lors de la duplication d'un plan. [#9 juin 2026]
- **Interface utilisateur :**
    - Barre de recherche avec autofocus dans les listes de mesures, indicateurs, actions et collectivités. [#29 juin 2026]
    - Amélioration de l'affichage du badge d'audit. [#24 juin 2026]
    - Ajout d'une primitive FloatingPanel non-modale pour les composants de l'interface. [#23 juin 2026]

### Évolutions techniques
- **Sécurité :**
    - Correction de plusieurs vulnérabilités de sécurité identifiées lors de tests d'intrusion (IDOR, SSRF, contrôle d'accès horizontal). [#12 juin 2026, #8 juin 2026]
    - Renforcement de la politique de sécurité du contenu (CSP). [#26 juin 2026]
    - Restriction de l'accès aux objets de stockage Supabase aux membres de la collectivité. [#12 juin 2026]
- **Architecture et Performance :**
    - Refactor de l'architecture de l'import de plans via l'IA, avec une séparation claire des responsabilités et une meilleure gestion des erreurs. [#4 juin 2026, #9 juin 2026]
    - Optimisation du chargement des données et suppression de dépendances inutiles (Fuse.js). [#8 juin 2026]
    - Amélioration de la gestion des états et des composants de l'interface utilisateur. [#10 juin 2026]
    - Mise à jour de Node.js vers la version 24.18.0 pour corriger une régression. [#25 juin 2026]
    - Mise en place de tests e2e parallèles pour accélérer les cycles de test. [#25 juin 2026]
- **Infrastructure :**
    - Mise à jour des dépendances (Next.js, eslint-config-next). [#12 juin 2026]

### Autres changements
- Documentation améliorée pour l'utilisation de l'IA par les agents. [#25 juin 2026]
- Ajout de jalons pour la bascule vers le nouveau référentiel TE. [#29 juin 2026]
- Amélioration de la gestion des erreurs et des logs.
- Nettoyage du code et refactoring de plusieurs composants.
- Mise à jour du schéma des préférences de la collectivité. [#25 juin 2026]
- Synchronisation des données CRM depuis les outils. [#8 juin 2026]
- Ajout de tests unitaires et d'intégration pour améliorer la couverture du code.
