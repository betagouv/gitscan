## Changelog : transports-sanitaires (30 derniers jours, au 29 septembre 2026)

### Résumé
Ce mois a été marqué par une montée en version majeure (v9.7.3) centrée sur la fiabilité des documents administratifs et la précision du simulateur. L'évolution majeure réside dans l'implémentation d'un système de "mapping documentaire" qui automatise et sécurise le remplissage des formulaires (Cerfa, DAP, PMT). Les règles de calcul liées aux situations médicales spécifiques (radiothérapie, EHPAD, etc.) ont été affinées pour garantir une simulation plus proche de la réalité.

### Évolutions fonctionnelles

**Formulaires et documents administratifs**
- Automatisation du pré-remplissage des formulaires Cerfa, DAP, PMT et S3141 grâce à un nouveau socle de mapping documentaire. [#14](https://github.com/betagouv/transports-sanitaires/issues/14)
- Intégration directe du texte médical intégral dans les formulaires Cerfa, supprimant la nécessité d'ajouter des annexes. [#12](https://github.com/betagouv/transports-sanitaires/issues/12)
- Amélioration de la lisibilité des adresses dans les documents PDF générés. [#14](https://github.com/betagouv/transports-sanitaires/issues/14)

**Simulation et expérience utilisateur**
- Amélioration de la précision de la saisie des informations médicales via une saisie directe. [#15](https://github.com/betagouv/transports-sanitaires/issues/15)
- Affichage des lieux déduits lors de l'étape de résultat de la simulation. [#11](https://github.com/betagouv/transports-sanitaires/issues/11)
- Requalification automatique de la convocation lorsque le trajet est modifié.
- Meilleure gestion de l'orientation vers la caisse d'assurance maladie pour le patient.

**Corrections de bugs**
- Résolution de plusieurs anomalies de calcul liées aux exceptions médicales (radiothérapie, transferts compatibles, séjours en EHPAD/USLD). [#6](https://github.com/betagouv/transports-sanitaires/issues/6), [#7](https://github.com/betagouv/transports-sanitaires/issues/7), [#8](https://github.com/betagouv/transports-sanitaires/issues/8)
- Correction de problèmes de cohérence sur les destinations d'urgence et les retours pénitentiaires. [#4](https://github.com/betagouv/transports-sanitaires/issues/4), [#5](https://github.com/betagouv/transports-sanitaires/issues/5)
- Correction de l'affichage des adresses et des totaux de permission (DAP) dans les documents. [#2](https://github.com/betagouv/transports-sanitaires/issues/2), [#9](https://github.com/betagouv/transports-sanitaires/issues/9)

### Évolutions techniques

**Architecture et Refactoring**
- Refonte de la structure du code pour isoler les modules de gestion des formulaires Cerfa.
- Réorganisation des dossiers internes (notamment le dossier `secretariat/`) pour une meilleure maintenance.
- Stabilisation du nommage des événements Matomo pour fiabiliser le suivi analytique.

**Qualité et Sécurité**
- Mise à jour de la bibliothèque `qs` pour corriger des vulnérabilités de sécurité (avis GHSA).
- Renforcement de la couverture de tests unitaires sur les nouveaux mécanismes de mapping documentaire (DAP, PMT, S3141).
- Mise à jour des recettes de tests pour accompagner les versions 9.7.x.

### Autres changements
- Refonte de la documentation technique avec une organisation par "connaissances" (`docs/knowledge/`) pour une divulgation progressive de l'information.
- Mise à jour régulière du README et de la documentation d'intégration.
