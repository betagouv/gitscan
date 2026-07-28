## Changelog : acces-cible (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations à la sécurité et à la stabilité de l'application, notamment en empêchant la suppression d'éléments critiques via l'interface et en corrigeant des erreurs liées à la gestion des requêtes réseau et des logs. Des améliorations de l'expérience utilisateur sont également incluses, comme l'affichage du nom d'utilisateur et l'amélioration de la détection des pages d'accessibilité.

### Évolutions fonctionnelles
- Le nom d'utilisateur est maintenant affiché sur la page profil ([#646](https://github.com/betagouv/acces-cible/issues/646)).
- Amélioration de la détection des pages d'accessibilité ([#610](https://github.com/betagouv/acces-cible/issues/610)).
- Liaison des audits aux utilisateurs pour un meilleur suivi.
- Ajout d'un concern `Privileged` aux modèles `Team` et `User` pour gérer les permissions spécifiques.
- Empêche la suppression des sites, audits et tags depuis l'interface utilisateur ([#637](https://github.com/betagouv/acces-cible/issues/637)).

### Évolutions techniques
- Correction d'une erreur de type `nil` pour le type de contenu ([#614](https://github.com/betagouv/acces-cible/issues/614)).
- Correction d'un problème de délai d'attente et d'inactivité du réseau ([#627](https://github.com/betagouv/acces-cible/issues/627)).
- Suppression de la colonne `name` de la table `sites` ([#641](https://github.com/betagouv/acces-cible/issues/641)).
- Suppression des logs Active Record envoyés à Sentry ([#621](https://github.com/betagouv/acces-cible/issues/621)).
- Mise en place d'une configuration et d'un workflow `release-please` pour automatiser les releases ([#623](https://github.com/betagouv/acces-cible/issues/623)).
- Ajout de `jemalloc` comme buildpack pour optimiser la gestion de la mémoire ([#591](https://github.com/betagouv/acces-cible/issues/591)).
- Isolation de la page dans un nouveau contexte pour un nettoyage plus efficace avec Ferrum ([#592](https://github.com/betagouv/acces-cible/issues/592)).

### Autres changements
- Mise à jour de l'adresse email de contact de l'application ([#618](https://github.com/betagouv/acces-cible/issues/618)).
- Blocage de davantage d'extensions de fichiers et de domaines de suivi.
- Nettoyage du fichier README.
- Suppression de scopes et de jobs récurrents inactifs.
- Correction d'un échec de test local `run_axe_on_homepage_spec` ([#609](https://github.com/betagouv/acces-cible/issues/609)).
