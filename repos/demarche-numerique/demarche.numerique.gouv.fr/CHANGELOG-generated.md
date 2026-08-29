## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'une modernisation majeure de son infrastructure technique avec le passage à Rails 8.1 et une refonte profonde de la gestion des formulaires pour garantir plus de fiabilité. Les utilisateurs et administrateurs profiteront d'une meilleure continuité de service lors des fusions de comptes, d'outils d'édition enrichis et d'une gestion plus robuste des fichiers et des données cartographiques.

### Évolutions fonctionnelles
- **Gestion des dossiers et affectations**
  - Exposition de l'historique des affectations de dossiers via l'API v2 [#13742](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13742).
  - Nouvelles capacités d'affectation de dossiers via l'API [#13744](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13744).
- **Administration et édition**
  - Amélioration de l'éditeur d'attestations et d'emails avec l'ajout d'un bouton "paragraphe" et une harmonisation des infobulles [#13625](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13625).
  - Possibilité de laisser le libellé d'une explication de champ vide pour plus de flexibilité [#13639](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13639).
- **Transferts et fusion de comptes**
  - Amélioration de la continuité lors des fusions de comptes : transfert automatique des dossiers, des rendez-vous, des notifications, des paramètres de procédure et des avis pour les experts [#12/08 commits].
  - Renommage de "demande de transfert" en "offre de transfert" pour une meilleure clarté sémantique [#13620](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13620).
- **Gestion des fichiers et cartographie**
  - Amélioration de la gestion des dossiers vides via la mise en cache des PDF générés [#13625](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13625).
  - Meilleure assistance lors des échecs d'upload (messages d'aide pour débloquer un envoi de fichier vide) [#13664](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13664).
  - Corrections sur les couches cartographiques (cadastres et RPG) et les filtres de recherche [#19/08 commits].
- **Messagerie**
  - Sécurisation de la traçabilité : impossibilité de supprimer les messages de modification de dossier [#13740](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13740).

### Évolutions techniques
- **Mise à jour majeure du framework**
  - Migration complète de l'application vers **Rails 8.1** [#13612](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13612).
- **Refonte de l'architecture des formulaires**
  - Refactorisation massive de la gestion des "types de champs" via l'utilisation du polymorphisme (STI). Cette modification permet d'isoler et de sécuriser la logique propre à chaque type de champ (date, nombre, texte, etc.) [#13662](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13662).
- **Optimisation des performances**
  - Résolution de nombreux problèmes de requêtes N+1, notamment sur les données géographiques et les appels GraphQL [#475698539, bb1793a0e].
  - Segmentation du trafic GraphQL pour un monitoring plus fin via Skylight [#13657](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13657).
- **Modernisation et nettoyage du code**
  - Migration massive des composants de l'interface utilisateur de HAML vers **ERB** [#13742](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13742).
  - Nettoyage de la base de données : suppression de colonnes obsolètes et retrait de la gestion des tâches via `delayed_job` [#13682](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13682).
- **Sécurité et robustesse**
  - Renforcement de la sécurité sur les téléchargements d'exports pour prévenir les attaques par traversée de chemin (path traversal) [#13669](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13669).
  - Durcissement de la gestion des images et des décodeurs (libvips) [#13626](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13626).

### Autres changements
- **Internationalisation (i18n)**
  - Extraction massive de chaînes de caractères codées en dur vers les fichiers de traduction pour faciliter la maintenance et la correction des textes [#13729](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13729).
- **Documentation**
  - Mise à jour de la documentation technique concernant les dépendances système (libvips) et les spécificités de l'API [#40c4a4, 12/08].
