## Changelog : acces-cible (30 derniers jours, au 20 juillet 2026)

### Résumé
Cette version apporte des améliorations de sécurité, de stabilité et de fonctionnalités. Les utilisateurs bénéficieront notamment d'une meilleure gestion des audits, d'une détection plus précise des pages accessibles et de corrections de bugs pour une expérience plus fluide. Des optimisations techniques ont également été réalisées pour améliorer les performances et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout de la possibilité de lier les audits aux utilisateurs.
- Amélioration de la détection des pages accessibles pour une analyse plus précise.
- Suppression de la colonne `name` de la table `sites` ([#641](https://github.com/betagouv/acces-cible/pull/641)).
- Ajout d'un en-tête `User-Agent` personnalisé pour les requêtes.
- Ajout d'un concern `Privileged` aux modèles `Team` et `User` pour gérer les permissions ([#639](https://github.com/betagouv/acces-cible/pull/639)).
- Empêche la suppression des sites, audits et tags depuis l'interface utilisateur ([#637](https://github.com/betagouv/acces-cible/pull/637)).

### Évolutions techniques
- Correction d'une erreur de type de contenu `nil` ([#614](https://github.com/betagouv/acces-cible/issues/614)).
- Correction d'un problème de délai d'attente et d'inactivité du réseau ([#627](https://github.com/betagouv/acces-cible/issues/627)).
- Suppression des logs Active Record envoyés à Sentry pour améliorer la performance et la sécurité ([#621](https://github.com/betagouv/acces-cible/issues/621)).
- Mise à jour de la configuration `release-please` et ajout du workflow associé ([#623](https://github.com/betagouv/acces-cible/pull/623)).
- Utilisation de `jemalloc` pour l'allocation mémoire ([#591](https://github.com/betagouv/acces-cible/issues/591)).
- Isolation de la page dans un nouveau contexte pour éviter les interférences et améliorer la stabilité ([#592](https://github.com/betagouv/acces-cible/issues/592)).

### Autres changements
- Mise à jour de l'adresse e-mail de contact d'AC ([#618](https://github.com/betagouv/acces-cible/issues/618)).
- Mise à jour de la documentation README pour plus de clarté ([#625](https://github.com/betagouv/acces-cible/issues/625)).
- Mise à jour de la documentation de l'aide pour les titres ([#602](https://github.com/betagouv/acces-cible/issues/602)).
- Blocage de davantage d'extensions de fichiers et de domaines de suivi ([#598](https://github.com/betagouv/acces-cible/issues/598)).
- Suppression des scopes inactifs et des jobs récurrents associés.
