## Changelog : passemarche (30 derniers jours, au 13 août 2026)

### Résumé
Cette période a été marquée par deux évolutions majeures : l'introduction de la possibilité de candidater en groupement (plusieurs entreprises ensemble) et la mise à disposition d'une synthèse PDF de la configuration pour les acheteurs. L'expérience utilisateur a également été affinée grâce à des corrections sur les formulaires et une mise en conformité des textes juridiques.

### Évolutions fonctionnelles
- **Gestion des groupements** : Introduction du mode de candidature en groupement, permettant de choisir le type de groupement juridique et de définir un mandataire [#484](https://github.com/datagouv/passemarche/pull/484), [#489](https://github.com/datagouv/passemarche/pull/489).
- **Synthèse de configuration** : Les acheteurs peuvent désormais générer et télécharger un document PDF récapitulant leur configuration de marché [#452](https://github.com/datagouv/passemarche/pull/452).
- **Amélioration de la gestion des lots** : Les exigences liées à un type de lot sont désormais automatiquement décochées si ce lot est retiré, et les lots sélectionnés sont inclus dans les notifications (webhooks) envoyées aux candidats [#465](https://github.com/datagouv/passemarche/pull/465), [#475](https://github.com/datagouv/passemarche/pull/475).
- **Conformité et rédaction** : Mise à jour des textes concernant les motifs d'exclusion pour répondre aux recommandations de la DAJ et ajout d'un rappel de ces motifs dans les attestations [#486](https://github.com/datagouv/passemarche/pull/486).
- **Corrections d'interface et de formulaires** :
    - Correction de la mémorisation des réponses "Non" sur les champs optionnels [#467](https://github.com/datagouv/passemarche/pull/467).
    - Clarification des messages d'erreur pour les marchés non encore publiés [#472](https://github.com/datagouv/passemarche/pull/472).
    - Ajustements visuels sur les boutons et les bandeaux d'erreur [#481](https://github.com/datagouv/passemarche/pull/481), [#482](https://github.com/datagouv/passemarche/pull/482).

### Évolutions techniques
- **Sécurité** : Mise à jour de Rails vers la version 8.1.3.1 pour corriger une vulnérabilité (CVE-2026-66066) [#485](https://github.com/datagouv/passemarche/pull/485).
- **Performance CI/CD** : Parallélisation des tests (RSpec et Cucumber) pour réduire le temps d'exécution des pipelines d'intégration [#451](https://github.com/datagouv/passemarche/pull/451).
- **Architecture et traçabilité** :
    - Refactorisation de la génération de PDF via un module commun pour plus de cohérence [#452](https://github.com/datagouv/passemarche/pull/452).
    - Mise en place de l'historisation (audit trail) des modifications de lots et des sélections d'attributs par les acheteurs [#458](https://github.com/datagouv/passemarche/pull/458).
- **Infrastructure API** : Standardisation de la génération des URLs via une configuration canonique pour garantir la fiabilité des webhooks et des appels API [#460](https://github.com/datagouv/passemarche/pull/460).

### Autres changements
- **Documentation** : Suppression de la synchronisation locale de la documentation vers le site des guides [#473](https://github.com/datagouv/passemarche/pull/473).
- **Nettoyage** : Suppression de code mort (méthodes inutilisées) [#468](https://github.com/datagouv/passemarche/pull/468).
