## Changelog : rapportnav2 (30 derniers jours, au 30 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'application, notamment l'ajout de la gestion des criées, des corrections de bugs concernant l'analyse des données, l'authentification et la sécurité, ainsi que des mises à jour de dépendances pour maintenir la stabilité et la sécurité du système. Des améliorations de la configuration de publication ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité de gestion des criées, incluant la liste des criées, les endpoints associés et l'interface d'administration. [#87347da](https://github.com/MTES-MCT/rapportnav2/commit/87347da58c97f5a9cf2fb406730f0494de19b785)
- Amélioration de l'opération de plongée dans le module de contrôle environnemental. [#1568282](https://github.com/MTES-MCT/rapportnav2/commit/156828246f9b683e5dce0c424f812a82a917004a)
- Correction d'un bug concernant l'ajout d'une nouvelle infraction lors de la création d'un nouveau contrôle. [#1325](https://github.com/MTES-MCT/rapportnav2/pull/1325)
- Correction d'un problème où l'API ne renvoyait pas toujours un résultat nul pour les sati. [#779ea05](https://github.com/MTES-MCT/rapportnav2/commit/779ea0554695f762469b518492984936869b469f)

### Évolutions techniques
- Refonte de la configuration `release-please-config.json` pour améliorer le processus de publication. [#55363a9](https://github.com/MTES-MCT/rapportnav2/commit/55363a9a0acb8691bfd3732b6fe02f357a8730c7), [#6a197bb](https://github.com/MTES-MCT/rapportnav2/commit/6a197bba656c74cd1d1d6d256f753ae9c199b34d), [#4e24402](https://github.com/MTES-MCT/rapportnav2/commit/4e2440284e72c410f6c1a09eb4fb52108c4097dd)
- Mise à jour de Spring Boot. [#165e74b](https://github.com/MTES-MCT/rapportnav2/commit/165e74b528e1fb775fa31c35404085c825870f04)
- Correction d'une boucle infinie causée par `isLoggedIn` dans `use-auth.ts`. [#6a09e0e](https://github.com/MTES-MCT/rapportnav2/commit/6a09e0e01b96be96b257788af02490b610d1381c)
- Amélioration de la sécurité en utilisant le hash de commit au lieu du tag pour la défense en profondeur. [#7b7d5b4](https://github.com/MTES-MCT/rapportnav2/commit/7b7d5b445f29f446f124462f2f70c83163888244)
- Correction d'un problème de troncature de la conversion en entier dans le calcul de la durée des analyses. [#27eaab8](https://github.com/MTES-MCT/rapportnav2/commit/27eaab87060f92329313f58f0f644c961110121f)
- Correction d'un problème de validation du schéma lors de la création de mission. [#58a0b86](https://github.com/MTES-MCT/rapportnav2/commit/58a0b86369612651151284268914779946683471)
- Correction d'un problème de fallback sur l'adresse pour l'utilisation de l'API d'établissement. [#d2edcf0](https://github.com/MTES-MCT/rapportnav2/commit/d2edcf067c68454537f5033a4c7340f62d686999)

### Autres changements
- Ajout d'un fichier `.trivyignore.yml` pour ignorer certains résultats lors de l'analyse de vulnérabilités. [#8556563](https://github.com/MTES-MCT/rapportnav2/commit/85565637d666d360548aa76cfad4cb31de154028)
- Mise à jour des dépendances frontend pour réduire les vulnérabilités. [#ffa4666](https://github.com/MTES-MCT/rapportnav2/commit/ffa4666895c94a228ce5d2000c31c96ead8dd485)
- Mise à jour de la dépendance `tools.jackson.core:jackson-core`. [#923725c](https://github.com/MTES-MCT/rapportnav2/commit/923725c813576262747f69187f843f46a147845f)
- Correction de problèmes liés à la configuration du cache HTML CSP. [#9239c35](https://github.com/MTES-MCT/rapportnav2/commit/9239c35cd4f628f91485f23129d3aa194d0c4c30)
- Mise à jour de Monitor-UI. [#2934f9b](https://github.com/MTES-MCT/rapportnav2/commit/2934f9b9f266231631f9874697f64a8981666297)
