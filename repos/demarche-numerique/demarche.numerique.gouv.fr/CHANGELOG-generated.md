## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 16/09/2026)

### Résumé
Ce mois a été marqué par une phase majeure de modernisation de la plateforme. Les efforts se sont concentrés sur trois axes : une amélioration significative de l'expérience utilisateur (interface de recherche, gestion des dossiers et pré-remplissage des données), un renforcement important de la sécurité (protection des comptes administrateurs et gestion des sessions) et une refonte technique profonde (mise à jour vers Rails 8.1 et modernisation des composants de l'application).

### Évolutions fonctionnelles
- **Messagerie et documents** : Augmentation de la limite de taille des pièces jointes à 200 Mo et amélioration des messages d'erreur lors des échecs d'envoi.
- **Gestion des dossiers** : 
    - Amélioration de l'affichage et de la sélection des "dossiers liés" pour les usagers (affichage enrichi et nouveaux composants de sélection) [#13298](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13298).
    - Correction de l'affichage des badges de partage sur les demandes de transfert.
- **Expérience utilisateur (UX/UI)** :
    - Refonte des filtres de recherche sur les pages de listes (utilisation d'accordéons DSFR, ajout de boutons de recherche et de filtres par email/domaine).
    - Amélioration de l'éditeur de texte (Tiptap) avec l'ajout de nouveaux outils (bouton paragraphe, info-bulles).
    - Mise à jour complète de la FAQ (corrections orthographiques, typographiques et fiabilisation des liens).
- **Pré-remplissage et connectivité** : 
    - Amélioration du pré-remplissage des données d'identité et du SIRET via ProConnect pour les usagers.
    - Renforcement de la gestion des jetons (tokens) de l'API Particulier avec des indicateurs visuels de validité et d'expiration.
- **Sécurité et Administration** :
    - Renforcement de la protection des comptes "Super Admin" (limitation des tentatives de codes OTP, ré-authentification quotidienne requise) [#13936](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13936).
    - Mise en place d'un registre de sessions pour permettre le suivi des connexions utilisateurs.
    - Amélioration de la recherche de procédures pour les administrateurs (par libellé ou numéro d'ID).

### Évolutions techniques
- **Modernisation de l'architecture** :
    - Migration de l'ensemble de la plateforme vers **Rails 8.1** [#13612](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13612).
    - Refonte massive du système de gestion des "Types de champs" via l'utilisation du polymorphisme (STI) pour une meilleure extensibilité [#13663](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13663).
    - Migration de la majorité des templates de HAML vers ERB pour s'aligner sur les standards modernes.
    - Refonte du système de gestion des modèles d'emails vers une structure centralisée en base de données [#13609](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13609).
- **Performances** :
    - Optimisation des requêtes GraphQL via le préchargement (preloading) des données liées (procédures, dossiers, descripteurs de champs).
    - Résolution de plusieurs problèmes de performance de type "N+1" sur les listes de dossiers, les étiquettes et les zones géographiques.
- **Sécurité et Infrastructure** :
    - Mise en place d'un environnement sécurisé (sandbox) pour l'exécution de commandes traitant des données externes non sécurisées [#13724](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13724).
    - Amélioration du monitoring et du regroupement des erreurs via Sentry.
    - Renforcement de la validation des jetons JWT pour les API.

### Autres changements
- **Documentation** : Mise à jour de la documentation technique (AGENTS.md) concernant les dépendances de l'environnement et les conventions de monitoring.
- **Maintenance** : Nettoyage de la base de données par la suppression de nombreuses colonnes obsolètes et de fonctionnalités (feature flags) n'étant plus utilisées.
