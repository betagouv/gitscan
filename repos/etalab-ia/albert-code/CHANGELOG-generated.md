## Changelog : albert-code (30 derniers jours, au 21 juillet 2026)

### Résumé
Ce mois-ci, Albert Code a connu des améliorations significatives en termes d'expérience utilisateur, de sécurité et de stabilité. L'accent a été mis sur la simplification de l'installation et de la configuration, l'intégration de l'authentification GitHub, et la correction de plusieurs problèmes critiques identifiés lors des phases de test internes. Le projet continue d'évoluer vers une solution de codage assisté par IA plus robuste et accessible.

### Évolutions fonctionnelles
- **Authentification GitHub :** Intégration de l'authentification GitHub pour l'installation et l'accès à la VM, simplifiant ainsi le processus de connexion. [#12](https://github.com/etalab-ia/albert-code/issues/12)
- **Gestion des modèles :** Ajout du modèle Qwen 3.6 27B aux modèles Albert embarqués. [#1](https://github.com/etalab-ia/albert-code/issues/1)
- **Amélioration de l'onboarding :** Refonte de l'expérience d'onboarding avec un wizard plus pédagogique, incluant des choix clairs pour l'activation des skills et de l'environnement de développement. [#6](https://github.com/etalab-ia/albert-code/issues/6)
- **Rafraîchissement des fichiers projet :** Mise à jour des fichiers projet figés, intégrant les dernières modifications d'OpenCode et ajoutant des garde-fous pour assurer la compatibilité. [#16](https://github.com/etalab-ia/albert-code/issues/16)
- **Gestion des erreurs :** Amélioration de la gestion des erreurs lors du lancement de projets non compatibles avec Albert. [#13](https://github.com/etalab-ia/albert-code/issues/13)
- **Documentation :** Mise à jour de la documentation (README, AGENTS.md) pour refléter les changements et fournir des informations plus claires sur l'utilisation d'Albert Code.

### Évolutions techniques
- **Intégration d'agent-vm :** Intégration complète d'agent-vm, permettant d'utiliser OpenCode uniquement et d'accéder aux outils de développement Chrome au niveau de l'environnement de développement. [#11](https://github.com/etalab-ia/albert-code/issues/11)
- **Refactoring de l'authentification :** Simplification de l'authentification GitHub, avec récupération du nom et de l'adresse e-mail à partir du Personal Access Token (PAT).
- **Amélioration de la gestion des compétences :** Optimisation de la synchronisation des compétences (skills) avec un système de cache et de liens symboliques.
- **Correction de bugs critiques :** Résolution de plusieurs bugs critiques identifiés lors des phases de test internes (T-FIX-1 à T-FIX-8), notamment liés à la configuration, à la suppression et à la gestion des clés.
- **Mode Dry-run :** Ajout d'un mode "dry-run" pour les tests et le sandbox.

### Autres changements
- **Documentation :** Mise à jour de la section "Dépannage" du README avec des informations sur les problèmes rencontrés lors des tests internes.
- **Améliorations UI :** Améliorations visuelles du wizard d'installation (bannière, spinner, compteur, récapitulatif). [#9](https://github.com/etalab-ia/albert-code/issues/9)
- **Clarification de la documentation :** Reformulation de l'usage de Mistral et suppression de la mention de gratuité dans le README.
- **Backlog :** Mise à jour du backlog avec la résolution de T1.7 et la création de T1.8.
