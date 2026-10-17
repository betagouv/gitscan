## Changelog : passemarche (30 derniers jours, au 12 octobre 2026)

### Résumé
Ce mois-ci, l'application a franchi une étape majeure dans la gestion des groupements d'entreprises. Les mandataires disposent désormais d'un tableau de bord complet pour piloter et soumettre la candidature de leur groupe, tandis que les co-traitants bénéficient d'un parcours d'invitation plus fluide et sécurisé. L'interface s'enrichit également d'un support pour la langue anglaise et d'une meilleure flexibilité sur la gestion des lots.

### Évolutions fonctionnelles
- **Gestion des groupements** :
    - Mise en place d'un tableau de bord de suivi et de soumission pour le mandataire [#526](https://github.com/datagouv/passemarche/issues/526).
    - Ajout d'un tableau récapitulatif des lots sur le dashboard avec des fenêtres de confirmation pour les retraits de lots ou de co-traitants [#536](https://github.com/datagouv/passemarche/issues/536).
    - Amélioration du parcours des co-traitants : création automatique de la candidature lors de l'acceptation de l'invitation et accès direct au suivi du groupement [#578](https://github.com/datagouv/passemarche/issues/578).
    - Possibilité pour le mandataire de soumettre l'intégralité de la candidature du groupement via un nouveau processus dédié [#574](https://github.com/datagouv/passemarche/issues/574).
- **Expérience utilisateur & Flexibilité** :
    - Ajout d'un sélecteur de langue (Français/Anglais) dans l'en-tête de l'application [#530](https://github.com/datagouv/passemarche/issues/530).
    - Introduction d'une option permettant de désactiver la limitation du nombre de lots par candidat [#630](https://github.com/datagouv/passemarche/issues/630).
    - Clarification des messages de confirmation lors de la transmission des candidatures à la plateforme [#622](https://github.com/datagouv/passemarche/issues/622).

### Évolutions techniques
- **Architecture & Refactoring** :
    - Migration des composants de gestion des lots et des membres du groupement vers des `ViewComponents` pour améliorer la modularité et la maintenance [#541](https://github.com/datagouv/passemarche/issues/541), [#540](https://github.com/datagouv/passemarche/issues/540), [#562](https://github.com/datagouv/passemarche/issues/562).
    - Refactorisation de la logique du parcours de création de groupement (wizard) [#526](https://github.com/datagouv/passemarche/issues/526).
    - Découpage du fichier CSS principal en fichiers thématiques par domaine pour une meilleure organisation du design [#539](https://github.com/datagouv/passemarche/issues/539).
- **Outils de développement** :
    - Optimisation des previews Lookbook et de leur intégration avec l'autoloading Zeitwerk [#554](https://github.com/datagouv/passemarche/issues/554), [#542](https://github.com/datagouv/passemarche/issues/542).

### Autres changements
- **Corrections diverses** :
    - Gestion des cas d'invitations expirées ou introuvables avec l'affichage de pages dédiées [#617](https://github.com/datagouv/passemarche/issues/617).
    - Corrections de bugs d'affichage (colonnes de grille), de redirections et d'encodage (PDF/UTF-8).
    - Corrections de typos et d'accords dans les messages de l'interface.
    - Finalisation et correction des traductions anglaises.
