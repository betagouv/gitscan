## Changelog : scalingo-watcher (30 derniers jours, au 05/10/2026)

### Résumé
Lancement de la première version publique de scalingo-watcher. Les récents développements se sont concentrés sur la stabilisation de l'outil, l'amélioration de la clarté des alertes de santé du parc applicatif et l'automatisation complète du cycle de vie des modèles (templates) pour garantir une maintenance simplifiée et sécurisée.

### Évolutions fonctionnelles
- Amélioration de la clarté des notifications de santé du parc applicatif via des messages plus explicites en TypeScript ([#13](https://github.com/incubateur-ademe/scalingo-watcher/issues/13)).

### Évolutions techniques
- **Automatisation des templates :** Mise en place d'un processus où le "starter" devient l'unique source de vérité, avec mise à jour automatique des versions lors des releases pour assurer la convergence du parc ([#15](https://github.com/incubateur-ademe/scalingo-watcher/issues/15), [#16](https://github.com/incubateur-ademe/scalingo-watcher/issues/16), [#17](https://github.com/incubateur-ademe/scalingo-watcher/issues/17)).
- **Sécurité et CI/CD :** Résolution des alertes de sécurité CodeQL et Dependabot ([#4](https://github.com/incubateur-ademe/scalingo-watcher/issues/4)) et ajustement de la période de quarantaine des mises à jour pour optimiser la sécurité ([#9](https://github.com/incubateur-ademe/scalingo-watcher/issues/9), [#12](https://github.com/incubateur-ademe/scalingo-watcher/issues/12)).
- **Gestion des environnements :** Correction du mapping des secrets d'environnement dans les composants du template ([#2](https://github.com/incubateur-ademe/scalingo-watcher/issues/2)).

### Autres changements
- Nettoyage de la documentation (suppression des références obsolètes à Python).
