## Changelog : territoires-en-transitions (30 derniers jours, au 17 septembre 2026)

### Résumé
Ce mois a été marqué par trois évolutions majeures : l'intégration complète de l'authentification via les fournisseurs d'identité (OIDC/ProConnect), le déploiement du nouveau processus d'instruction pour les PCAET (permettant un suivi en trois étapes et un tableau de bord dédié), et la transition vers le nouveau référentiel CR. La plateforme est devenue plus robuste avec un système de dépôt de documents sécurisé et une interface utilisateur plus intuitive et accessible.

### Évolutions fonctionnelles

**Authentification et Gestion des Utilisateurs**
- Mise en œuvre de la connexion et de l'inscription via les fournisseurs d'identité OIDC (ProConnect et MonCompteAdeme).
- Automatisation de l'affectation des agents à leur service respectif lors de la connexion.
- Amélioration du parcours d'invitation et de liaison d'identité pour une gestion plus fluide des comptes.

**Instruction PCAET et Démarches**
- Nouveau parcours d'instruction en trois étapes pour les dossiers PCAET, avec un tableau de bord dédié pour suivre les demandes d'avis.
- Ouverture des dossiers d'instruction aux services déconcentrés (DREAL, DDT) et aux services nationaux/régionaux.
- Amélioration de la visibilité des dossiers pour les collectivités : accès aux avis, révision des pièces et suivi de l'avancement.
- Intégration de l'IA pour l'analyse des plans par levier et la classification automatique des fiches.

**Référentiels et Scoring**
- Déploiement de la bascule vers le référentiel CR avec une modale de confirmation et une gestion améliorée de la navigation (affichage des référentiels archivés).
- Amélioration de l'export des scores incluant désormais une feuille de "Personnalisation".
- Mise à jour des indicateurs et des libellés pour plus de clarté dans le suivi des mesures.

**Gestion des Documents**
- Nouveau système de dépôt de documents sécurisé utilisant des jetons signés et un transport résumable.
- Amélioration de la bibliothèque de documents : gestion des droits de lecture synchronisée avec le backend et possibilité de reclasser les documents.

**Interface Utilisateur (UI/UX)**
- Ajout de nouveaux composants : boutons "Split Button", variantes de boutons "Danger" et boutons de lien.
- Amélioration de l'accessibilité des tableaux et de la navigation (en-têtes de colonnes fixes, indicateurs de tri visibles).
- Optimisation des bannières d'information avec mémorisation de la fermeture.

### Évolutions techniques

**Infrastructure et CI/CD**
- Migration majeure de la stratégie de déploiement : remplacement d'Earthly par des Dockerfiles natifs pour les applications.
- Mise en place de Nx Cloud pour optimiser les performances des workflows de CI.
- Optimisation des tests E2E via le partitionnement (sharding) et amélioration de la visibilité des logs de tâches.

**Architecture et Backend**
- Refactorisation importante des modules "Référentiels" et "Documents" pour une meilleure séparation des responsabilités.
- Migration de la lecture de l'arborescence des plans vers tRPC pour remplacer les vues Supabase.
- Amélioration de la gestion des sessions en distinguant les états (anonyme, connecté, session en cours).
- Renforcement de la sécurité des recherches en échappant les caractères spéciaux (jokers LIKE) côté backend.

### Autres changements

**Documentation**
- Mise à jour importante des ADR (Architecture Decision Records) concernant le déploiement, la gestion de la périodicité des indicateurs et la sortie d'Earthly.
- Amélioration de la documentation sur les spécifications de géocodage.

**Maintenance et Nettoyage**
- Suppression de workflows obsolètes et de code mort.
- Nettoyage des labels et uniformisation des nomenclatures (passage au camelCase pour plusieurs modèles de données).
- Correction de divers bugs d'affichage et de typage suite aux retours de revue [#5053](https://github.com/incubateur-ademe/territoires-en-transitions/pull/5053).
