## Changelog : just-code (30 derniers jours, au 26 septembre 2026)

### Résumé
Ce mois a marqué une étape majeure dans la structuration de `just-code`, passant d'un prototype expérimental à un outil plus robuste et sécurisé. Les évolutions se sont concentrées sur la simplification de la mise en route des projets (nouvelle commande d'initialisation), le renforcement de la sécurité (détection automatique de secrets et isolation des identifiants) et l'élargissement de la compatibilité, notamment avec un support accru pour Windows et l'ajout de machines virtuelles macOS pour les besoins liés à Xcode.

### Évolutions fonctionnelles
- **Initialisation et configuration :**
  - Introduction de la commande `just-code init` pour configurer rapidement un nouveau projet [#97](https://github.com/etalab-ia/just-code/issues/97).
  - Mise en place d'un moteur de configuration minimale et typée pour garantir la cohérence des projets [#96](https://github.com/etalab-ia/just-code/issues/96), [#79](https://github.com/etalab-ia/just-code/issues/79).
  - Ajout d'un mode d'exécution avec isolation complète (`--isolation full`) pour une sécurité maximale [#44](https://github.com/etalab-ia/just-code/issues/44).
- **Sécurité utilisateur :**
  - Protection contre les fuites de données : le démarrage est désormais refusé si des secrets sont détectés dans l'espace de travail [#42](https://github.com/etalab-ia/just-code/issues/42).
  - Gestion améliorée des identifiants : possibilité de lier plusieurs comptes et de révoquer des accès explicitement [#87](https://github.com/etalab-ia/just-code/issues/87).
- **Nouveaux environnements :**
  - Support des VM macOS via Tart, permettant l'exécution d'agents dans des environnements compatibles Xcode [#2](https://github.com/etalab-ia/just-code/issues/2).

### Évolutions techniques
- **Gestion des Runtimes et Isolation :**
  - Ajout du backend `agent-vm` basé sur Lima pour une alternative flexible aux microVMs [#38](https://github.com/etalab-ia/just-code/issues/38).
  - Amélioration de l'isolation de Microsandbox, incluant désormais une isolation complète par défaut [#94](https://github.com/etalab-ia/just-code/issues/94).
  - Refactorisation majeure du cycle de vie des projets et des runtimes pour permettre des redémarrages non destructifs [#82](https://github.com/etalab-ia/just-code/issues/82), [#81](https://github.com/etalab-ia/just-code/issues/81).
- **Architecture et Sécurité système :**
  - Sécurisation du stockage des identifiants : les credentials sont désormais stockés en dehors des dossiers de projets pour éviter toute fuite accidentelle [#86](https://github.com/etalab-ia/just-code/issues/86).
  - Portage natif en Go de la logique de gestion des runtimes (Tart, Docker, Microsandbox), supprimant la dépendance aux scripts shell pour plus de stabilité.
- **Compatibilité Windows :**
  - Travaux intensifs pour assurer le support natif de Windows via le runtime Microsandbox [#16](https://github.com/etalab-ia/just-code/issues/16).
- **CI/CD et Qualité :**
  - Automatisation du versionnage et de la publication des binaires via `release-please`.
  - Mise en place de builds d'artefacts macOS à la demande sur les Pull Requests.

### Autres changements
- **Documentation :** Refonte complète du README pour mieux accompagner l'utilisateur, ajout de guides de démarrage rapide pour Windows et mise à jour des plans d'implémentation.
- **Qualité du code :** Intégration d'un hook `pre-commit` utilisant `gitleaks` pour prévenir la soumission de secrets par les développeurs [#12](https://github.com/etalab-ia/just-code/issues/12).
