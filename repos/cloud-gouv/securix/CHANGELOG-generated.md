## Changelog : securix (30 derniers jours, au 02 octobre 2026)

### Résumé
Ce mois-ci, SecurixOS a bénéficié d'améliorations majeures visant à renforcer la fiabilité des mises à jour automatiques et la robustesse du système. L'expérience utilisateur a été affinée avec de meilleures options de configuration de l'interface et de l'installation, tandis que la documentation a été intégralement refondue pour offrir un support bilingue (français/anglais) complet.

### Évolutions fonctionnelles
- **Sécurité et interface** : Masquage des comptes administrateurs sur l'écran de connexion SDDM pour limiter l'exposition des comptes privilégiés [#265](https://github.com/cloud-gouv/securix/pull/265).
- **Interface de bureau** : Amélioration de la gestion des raccourcis clavier sous l'environnement Sway via l'utilisation des codes de touches (keycode) [#262](https://github.com/cloud-gouv/securix/pull/262).
- **Réseau** : La gestion des tunnels SSH via le proxy HTTP est désormais sécurisée et conditionnée par l'option `auth.sshForward`.
- **Installation** : Correction d'une erreur logique dans le terminal d'auto-installation concernant le saut des vérifications préliminaires [#267](https://github.com/cloud-gouv/securix/pull/267).

### Évolutions techniques
- **Mises à jour automatiques** : Optimisation du processus de mise à jour avec une stratégie de tentatives exponentielles (backoff) et suppression systématique des anciennes générations après un succès [#276](https://github.com/cloud-gouv/securix/pull/276), [#277](https://github.com/cloud-gouv/securix/pull/277).
- **Réseau (IPsec)** : Amélioration de la correspondance des noms de domaine (DNs) pour l'IPsec, permettant une identification indépendante de l'ordre des éléments [#279](https://github.com/cloud-gouv/securix/pull/279).
- **Optimisation matérielle** : Ajustement du gestionnaire de fréquence CPU pour assurer un fonctionnement optimal sur les machines de type x13 [#273](https://github.com/cloud-gouv/securix/pull/273).
- **Maintenance Nix** : Résolution de plusieurs erreurs d'évaluation Nix introduites lors de modifications récentes [#269](https://github.com/cloud-gouv/securix/pull/269).
- **Tests** : Correction d'une condition de concurrence (race condition) dans les tests du portail.

### Autres changements
- **Documentation** : Refonte complète de la documentation pour un support bilingue (français/anglais), incluant de nouveaux guides d'ingénierie et de déploiement, l'ajout de diagrammes et le support de Mermaid.
