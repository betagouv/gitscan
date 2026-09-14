## Changelog : mon-indemnisation-justice (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, l'application a franchi des étapes importantes, notamment sur le parcours de gestion des bris de porte avec l'ajout de nouveaux formulaires et d'exports PDF. Une refonte technique majeure a été opérée pour simplifier le code et renforcer la fiabilité du système, accompagnée d'une mise à jour complète des technologies de base (PHP, Symfony, Node.js).

### Évolutions fonctionnelles
- **Gestion des dossiers et formulaires** : Introduction du formulaire de déclaration et du téléversement de la DA ([#169](https://github.com/betagouv/mon-indemnisation-justice/pull/169)) et possibilité d'exporter les dossiers FIP3 au format PDF ([#170](https://github.com/betagouv/mon-indemnisation-justice/pull/170)).
- **Amélioration de la gestion documentaire** : Conversion automatique des documents requis en PDF et gestion intelligente des fichiers incompatibles pour garantir la génération des dossiers.
- **Nouvelles capacités de consultation** : Ajout de la prévisualisation des fichiers signés, affichage des motifs de clôture et enrichissement de la recherche par type de dossier.
- **Corrections d'expérience utilisateur** : Résolution de problèmes d'affichage des PDF sur Edge, correction des doublons lors de l'affectation et intégration des codes départements dans les courriers.

### Évolutions techniques
- **Refonte de l'architecture frontend** : Migration vers une architecture sans MobX, Valtio ou date-fns. La logique métier (signature, décision, clôture, attribution) est désormais déléguée à l'API pour plus de robustesse.
- **Mise à jour de la stack technologique** : Montée de version majeure vers PHP 8.5, Symfony 8.1 et Node.js 24.
- **Optimisation de la génération de documents** : Stabilisation du moteur de rendu via l'utilisation de Firefox (via Puppeteer) et amélioration des performances grâce à une meilleure gestion du cache et des tentatives de reconnexion (retries).
- **Infrastructure** : Mise à jour des GitHub Actions pour la CI/CD.

### Autres changements
- **Contenu et conformité** : Uniformisation des paragraphes de responsabilité et correction des trames de documents.
