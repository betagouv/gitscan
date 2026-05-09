## Changelog : rapportnav2 (30 derniers jours, au 7 mai 2026)

### Résumé
Cette version apporte des améliorations à la recherche d'établissements, des corrections de sécurité et de stabilité, ainsi que des mises à jour de l'infrastructure et des dépendances. L'outil a également bénéficié d'améliorations continues du pipeline CI/CD pour une meilleure qualité et rapidité des livraisons.

### Évolutions fonctionnelles
- Amélioration de la recherche d'établissements ([d6abde6](https://github.com/MTES-MCT/rapportnav2/commit/d6abde6d85e5ca95115d5069d1f551fa3afa3a5a)).
- Ajout de la liste des criées et des endpoints associés, ainsi que de l'interface d'administration correspondante ([87347da](https://github.com/MTES-MCT/rapportnav2/commit/87347da7720f36301830795448367078726692f7)).
- Correction pour permettre l'ajout de nouvelles infractions lors de la création d'un nouveau contrôle ([32f22a7](https://github.com/MTES-MCT/rapportnav2/commit/32f22a7c361f4053b1330b214817167233979185)).

### Évolutions techniques
- Mise à jour de la version de Vite à la version 8 ([8937f8f](https://github.com/MTES-MCT/rapportnav2/commit/8937f8ff92695852f2364cb690fe43d963f1e142)).
- Refonte du pipeline CI/CD pour utiliser gitlab-forge ([7b6bf05](https://github.com/MTES-MCT/rapportnav2/commit/7b6bf053678d0989396071b7bc60b81c0b2b9111)).
- Mise à jour de plusieurs dépendances : Kotlin, Flyway, Spring Boot, Monitor-UI, Gradle.
- Mise à jour du container PostgreSQL à la version 15.17 ([a627c05](https://github.com/MTES-MCT/rapportnav2/commit/a627c058cbc449cd19485d43d148e16d93a1baa1)).
- Amélioration de la configuration de SonarQube et correction de problèmes liés à la couverture du code.
- Mise à jour de la configuration de Trivy et de dependency-check pour améliorer la sécurité.

### Autres changements
- Suppression d'un fichier `.env` obsolète ([cc63919](https://github.com/MTES-MCT/rapportnav2/commit/cc6391941894949f59f4309859f2669954886f6b)).
- Mise à jour des suppressions de CVE pour éviter les faux positifs ([46dabc6](https://github.com/MTES-MCT/rapportnav2/commit/46dabc691980f619331b7681458446201f215616)).
- Correction de problèmes liés à la configuration de SonarQube et à l'analyse du code.
- Mise à jour des snapshots de tests.
- Correction de problèmes liés à la validation du schéma de création de mission.
- Correction de l'utilisation de variables d'environnement pour l'utilisateur et le mot de passe de la base de données.
