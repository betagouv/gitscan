## Changelog : acces-cible (30 derniers jours, au 28 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations de sécurité avec l'ajout d'un système de limitation de requêtes, des corrections de bugs pour améliorer la stabilité et l'expérience utilisateur, et des ajustements techniques pour faciliter la maintenance et le déploiement de l'application. Des restrictions d'édition et de suppression d'éléments ont été ajoutées via l'interface utilisateur pour renforcer la sécurité.

### Évolutions fonctionnelles
- Ajout d'un système de limitation de requêtes pour prévenir les abus et améliorer la disponibilité de l'application. [#659](https://github.com/betagouv/acces-cible/issues/659)
- Le nom d'utilisateur est maintenant affiché sur la page profil. [#646](https://github.com/betagouv/acces-cible/issues/646)
- Amélioration de la détection des pages d'accessibilité. [#610](https://github.com/betagouv/acces-cible/issues/610)
- Liaison des audits aux utilisateurs pour une meilleure traçabilité.
- Possibilité de lier des audits aux utilisateurs.
- Prévention de la modification des sites et des tags depuis l'interface utilisateur. [#643](https://github.com/betagouv/acces-cible/issues/643)
- Prévention de la suppression des sites, audits et tags depuis l'interface utilisateur. [#637](https://github.com/betagouv/acces-cible/issues/637)

### Évolutions techniques
- Suppression de la colonne `name` de la table `sites`. [#641](https://github.com/betagouv/acces-cible/issues/641)
- Refactorisation du code de parsing des liens, suppression de `LinkList`. [#636](https://github.com/betagouv/acces-cible/issues/636)
- Ajout d'un "concern" `Privileged` aux modèles `Team` et `User` pour gérer les privilèges. [#639](https://github.com/betagouv/acces-cible/issues/639)
- Suppression des logs Active Record envoyés à Sentry. [#621](https://github.com/betagouv/acces-cible/issues/621)
- Mise à jour de la configuration de `release-please` et ajout du workflow associé. [#623](https://github.com/betagouv/acces-cible/issues/623)
- Ajout de `jemalloc` comme buildpack pour optimiser la gestion de la mémoire. [#591](https://github.com/betagouv/acces-cible/issues/591)
- Isolation de la page dans un nouveau contexte pour un nettoyage plus efficace avec Ferrum. [#592](https://github.com/betagouv/acces-cible/issues/592)
- Correction d'une erreur de type de contenu `nil`. [#614](https://github.com/betagouv/acces-cible/issues/614)
- Correction d'un problème de timeout réseau. [#627](https://github.com/betagouv/acces-cible/issues/627)

### Autres changements
- Mise à jour de l'adresse email de contact d'AC. [#618](https://github.com/betagouv/acces-cible/issues/618)
- Blocage de davantage d'extensions de fichiers et de domaines de tracking. [#598](https://github.com/betagouv/acces-cible/issues/598)
- Nettoyage du fichier README. [#625](https://github.com/betagouv/acces-cible/issues/625)
- Suppression de scopes inactifs et des jobs récurrents associés.
- Mises à jour de dépendances (googleapis/release-please-action, minor group updates).
- Publication des versions 1.1.0 et 1.1.1.
