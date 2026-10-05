## Changelog : just-code (30 derniers jours, au 02/10/2026)

### Résumé
Ce mois a marqué une étape majeure dans la maturité de just-code, passant d'un prototype basé sur Docker à un environnement multi-runtimes robuste et sécurisé. Le projet supporte désormais Windows et propose une isolation renforcée par défaut. L'expérience utilisateur a été simplifiée grâce à un nouveau processus d'initialisation et une interface en ligne de commande (TUI) plus fluide, tout en garantissant une gestion sécurisée des identifiants et des secrets.

### Évolutions fonctionnelles
- **Gestion des projets :** Introduction de la gestion des "skills" projet épinglées [#113](https://github.com/etalab-ia/just-code/issues/113) et d'un nouveau flux d'initialisation via la commande `just-code init` [#97](https://github.com/etalab-ia/just-code/issues/97), incluant un moteur de configuration minimale [#96](https://github.com/etalab-ia/just-code/issues/96) et une assistance au lancement [#98](https://github.com/etalab-ia/just-code/issues/98).
- **Interface utilisateur (TUI) :** Amélioration de l'expérience de reprise de session lors de l'attachement [#102](https://github.com/etalab-ia/just-code/issues/102) et correction des erreurs de lancement initial [#103](https://github.com/etalab-ia/just-code/issues/103).
- **Authentification et Identité :** Support de liaisons d'identifiants multiples avec possibilité de révocation [#87](https://github.com/etalab-ia/just-code/issues/87) et stockage sécurisé des identifiants en dehors des projets [#86](https://github.com/etalab-ia/just-code/issues/86).
- **Compatibilité OS :** Support officiel de Windows via le runtime Microsandbox [#16](https://github.com/etalab-ia/just-code/issues/16).
- **Intégration GitHub :** Activation du workflow pour les invités approuvés [#105](https://github.com/etalab-ia/just-code/issues/105).

### Évolutions techniques
- **Sécurité et Isolation :** Activation de l'isolation complète par défaut pour Microsandbox [#94](https://github.com/etalab-ia/just-code/issues/94), mise en place d'un scan de secrets dans les workspaces [#42](https://github.com/etalab-ia/just-code/issues/42) et durcissement du contrôle des montages de fichiers [#100](https://github.com/etalab-ia/just-code/issues/100).
- **Diversification des Runtimes :** Ajout du backend `agent-vm` (basé sur Lima) [#38](https://github.com/etalab-ia/just-code/issues/38) et du runtime macOS via Tart [#2](https://github.com/etalab-ia/just-code/issues/2).
- **Refactoring et Performance :** Portage massif des composants (Docker, Microsandbox, Tart) en Go pour une meilleure intégration et performance, et intégration directe du SDK Microsandbox.
- **Gestion du Cycle de Vie :** Implémentation de la réconciliation et du redémarrage non destructif des runtimes [#7](https://github.com/etalab-ia/just-code/issues/7) et mise à jour du runtime Microsandbox vers la v0.7.3 [#107](https://github.com/etalab-ia/just-code/issues/107).
- **Moteur de Configuration :** Passage à une résolution typée avec gestion des schémas et traçabilité de la provenance des paramètres [#4](https://github.com/etalab-ia/just-code/issues/4).

### Autres changements
- **Documentation :** Refonte complète du README pour un meilleur accompagnement utilisateur et ajout de guides de démarrage rapide pour Windows.
- **Qualité logicielle :** Intégration de `gitleaks` en tant que hook `pre-commit` pour prévenir la fuite accidentelle de secrets.
