## Changelog : complements-alimentaires (30 derniers jours, au 11 septembre 2026)

### Résumé
Cette période a été marquée par une stabilisation importante de la plateforme. Les efforts se sont concentrés sur la correction de bugs critiques (erreurs 404, problèmes de vérification d'email et de téléchargement de fichiers) et sur l'amélioration de l'expérience de navigation via des filtres plus souples. Parallèlement, l'infrastructure a été renforcée pour garantir une meilleure fiabilité des services, notamment pour l'envoi des emails et l'authentification.

### Évolutions fonctionnelles
- **Correction de bugs de navigation** : Résolution des erreurs 404 sur les pages d'instruction, de visa et de contrôle lorsqu'aucun déclarant n'est associé à une déclaration ([#3081](https://github.com/betagouv/complements-alimentaires/pull/3081), [#3071](https://github.com/betagouv/complements-alimentaires/pull/3071)).
- **Amélioration des filtres** : Possibilité de réinitialiser les filtres dans le tableau des entreprises et dans la liste des compléments alimentaires ([#3066](https://github.com/betagouv/complements-alimentaires/pull/3066)).
- **Fiabilisation des processus utilisateurs** : Correction du bug lié à la vérification de l'adresse email ([#3095](https://github.com/betagouv/complements-alimentaires/pull/3095)) et du filtre de statut ([#3072](https://github.com/betagouv/complements-alimentaires/pull/3072)).
- **Gestion des documents** : Correction des liens de téléchargement pour les exports Excel ([#3064](https://github.com/betagouv/complements-alimentaires/pull/3064)) et les certificats PDF ([#3034](https://github.com/betagouv/complements-alimentaires/pull/3034)).
- **Interface utilisateur** : Mise à jour des graphiques à barres et réintégration de certaines statistiques via le composant DSFR ([#3073](https://github.com/betagouv/complements-alimentaires/pull/3073)).

### Évolutions techniques
- **Optimisation de la messagerie** : Passage à un envoi d'emails asynchrone (via Brevo), mise en place de mécanismes de tentatives automatiques (retry) et journalisation des échecs dans Sentry ([#3074](https://github.com/betagouv/complements-alimentaires/pull/3074)).
- **Évolution de l'authentification** : Refonte de l'architecture liée à ProConnect, incluant la gestion de la date de dernière connexion ([#3023](https://github.com/betagouv/complements-alimentaires/pull/3023)).
- **Infrastructure et DevOps** : Intégration de Redis et Celery dans l'environnement Docker et mise à jour de la configuration Vite ([#3065](https://github.com/betagouv/complements-alimentaires/pull/3065)).

### Autres changements
- **Sécurité** : Ajout du fichier `security.txt` pour informer sur les politiques de signalement de vulnérabilités ([#3106](https://github.com/betagouv/complements-alimentaires/pull/3106)).
- **Documentation** : Ajout de nouveaux éléments de documentation technique et fonctionnelle.
