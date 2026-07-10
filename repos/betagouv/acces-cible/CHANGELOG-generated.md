## Changelog : acces-cible (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette version apporte des améliorations à la détection des pages accessibles, la liaison des audits aux utilisateurs, et la configuration du projet (release-please, email de contact). Des corrections de bugs ont également été implémentées, notamment concernant les logs Sentry et les tests.

### Évolutions fonctionnelles
- Amélioration de la détection des pages accessibles ([#610](https://github.com/betagouv/acces-cible/issues/610)).
- Liaison des audits aux utilisateurs, permettant un meilleur suivi des responsabilités.
- Ajout d'un en-tête `User-Agent` personnalisé pour les requêtes ([#601](https://github.com/betagouv/acces-cible/issues/601)).

### Évolutions techniques
- Mise à jour de la configuration Docker pour utiliser le Dockerfile principal ([#547](https://github.com/betagouv/acces-cible/issues/547)).
- Suppression des colonnes `url` et `current` de la table `audits` pour simplifier la structure de données ([#582](https://github.com/betagouv/acces-cible/issues/582), [#580](https://github.com/betagouv/acces-cible/issues/580)).
- Suppression de dépendances obsolètes (Omniauth fork).
- Amélioration de la gestion des tests (mocking Axe checks).
- Ajout de `jemalloc` pour optimiser la gestion de la mémoire ([#591](https://github.com/betagouv/acces-cible/issues/591)).
- Configuration de `release-please` pour automatiser les releases ([#623](https://github.com/betagouv/acces-cible/issues/623)).

### Autres changements
- Mise à jour de la documentation pour les en-têtes d'aide ([#602](https://github.com/betagouv/acces-cible/issues/602)).
- Modification de l'adresse email de contact de l'application ([#618](https://github.com/betagouv/acces-cible/issues/618)).
- Blocage de certaines extensions de fichiers et domaines de tracking ([#598](https://github.com/betagouv/acces-cible/issues/598)).
- Suppression des logs Active Record envoyés à Sentry ([#621](https://github.com/betagouv/acces-cible/issues/621)).
- Correction d'une erreur de test local (`run_axe_on_homepage_spec`) ([#609](https://github.com/betagouv/acces-cible/issues/609)).
