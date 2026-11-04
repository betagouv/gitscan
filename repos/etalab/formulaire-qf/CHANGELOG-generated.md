## Changelog : formulaire-qf (30 derniers jours, au 03 novembre 2026)

### Résumé
Les évolutions de ce mois se sont concentrées sur deux axes majeurs : le renforcement de la protection des données personnelles et la correction de plusieurs parcours utilisateurs. Des mesures importantes ont été prises pour éviter que des informations sensibles (identité, quotient familial) ne soient transmises par erreur aux outils de suivi technique, tout en stabilisant les interactions avec FranceConnect et les services de transmission DataPass.

### Évolutions fonctionnelles
- **Correction de parcours :** Résolution de bugs impactant le parcours FranceConnect ([#409](https://github.com/etalab/formulaire-qf/pull/409)) et le bouton de retour vers le site de la collectivité ([#412](https://github.com/etalab/formulaire-qf/pull/412)).
- **Gestion des erreurs :** Amélioration de l'affichage des messages d'erreur lors des échecs de transmission (notamment avec HubEE) pour une meilleure compréhension par l'utilisateur ([#404](https://github.com/etalab/formulaire-qf/pull/404)).
- **Alertes DataPass :** Mise en place d'alertes pour signaler les dossiers incomplets, comme l'absence de numéro de téléphone ([#405](https://github.com/etalab/formulaire-qf/pull/405)).
- **Fiabilité des pages :** Correction de problèmes sur les pages de confirmation et de transmission ([#403](https://github.com/etalab/formulaire-qf/pull/403), [#402](https://github.com/etalab/formulaire-qf/pull/402)).

### Évolutions techniques
- **Sécurité & Confidentialité :** Travail intensif de réduction des fuites de données personnelles (PII) vers l'outil de monitoring Sentry. Les identités, emails de collectivités et données de quotient familial sont désormais systématiquement exclus des logs et des traces d'erreurs ([#406](https://github.com/etalab/formulaire-qf/pull/406)).
- **Sécurité des dépendances :** Mise à jour de plusieurs bibliothèques critiques pour corriger des vulnérabilités (loofah, rack, addressable, crass) ([#424](https://github.com/etalab/formulaire-qf/pull/424), [#420](https://github.com/etalab/formulaire-qf/pull/420), [#416](https://github.com/etalab/formulaire-qf/pull/416)).
- **CI/CD :** Renforcement de la chaîne de tests avec l'exécution systématique sur chaque Pull Request et le blocage automatique des déploiements en cas de vulnérabilités détectées dans les dépendances ([#421](https://github.com/etalab/formulaire-qf/pull/421)).
- **Maintenance :** Mise à jour de l'environnement Ruby (version 4.0.9) et optimisation de l'environnement de développement (suppression de Spring).

### Autres changements
- **Documentation :** Création et enrichissement du fichier `CLAUDE.md` pour centraliser les conventions et commandes du projet.
- **Expérience développeur :** Ajout de nouveaux scripts pour faciliter le travail sur des branches isolées via les *worktrees*.
