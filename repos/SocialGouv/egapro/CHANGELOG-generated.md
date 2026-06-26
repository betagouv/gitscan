## Changelog : egapro (30 derniers jours, au 25 juin 2026)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans le parcours de conformité et l'administration, ainsi que sur l'ajout de nouvelles fonctionnalités statistiques et d'analyse. Des efforts ont également été déployés pour renforcer la sécurité et la conformité, notamment en intégrant Matomo avec une exemption CNIL.

### Évolutions fonctionnelles
- **Parcours de conformité :** Lecture seule du parcours de conformité pour certaines étapes [#3494](https://github.com/SocialGouv/egapro/issues/3494) et [#3755](https://github.com/SocialGouv/egapro/issues/3755).
- **Espace personnel :** Correction des libellés d'étape de rémunération pour une meilleure clarté [#3761](https://github.com/SocialGouv/egapro/issues/3761).
- **Avis CSE :** Refonte complète des pages d'avis du CSE [#3639](https://github.com/SocialGouv/egapro/issues/3639).
- **Administration :** Affichage du récapitulatif de la déclaration sur la page de détail de l'administration [#3437](https://github.com/SocialGouv/egapro/issues/3437) et [#3590](https://github.com/SocialGouv/egapro/issues/3590).  Amélioration du layout et ajout d'un dashboard de statistiques [#3586](https://github.com/SocialGouv/egapro/issues/3586).
- **Statistiques :** Ajout de comptages d'engagement CSE et du nombre d'utilisateurs par entreprise [#3756](https://github.com/SocialGouv/egapro/issues/3756).  Nouvelle distribution des scores publics (K7) [#3551](https://github.com/SocialGouv/egapro/issues/3551).
- **Authentification :** Préservation de l'URL cible lors de la redirection après la connexion [#3718](https://github.com/SocialGouv/egapro/issues/3718).
- **Analytique :** Intégration de Matomo avec une exemption de consentement CNIL [#3655](https://github.com/SocialGouv/egapro/issues/3655) et implémentation d'un plan de tracking Matomo pour les événements client et la documentation [#3625](https://github.com/SocialGouv/egapro/issues/3625).  Tracking des événements du modèle indicateur 7 et des liens d'aide [#3707](https://github.com/SocialGouv/egapro/issues/3707).
- **Gestion des fichiers :** Possibilité d'assigner des noms de fichiers générés [#3643](https://github.com/SocialGouv/egapro/issues/3643).

### Évolutions techniques
- **CI/CD :** Ajout d'un agent e2e-dev en fin de pipeline [#3654](https://github.com/SocialGouv/egapro/issues/3654). Ajout d'une vérification du journal monotone pour éviter les sauts de migration silencieux [#3557](https://github.com/SocialGouv/egapro/issues/3557) et [#3560](https://github.com/SocialGouv/egapro/issues/3560). Suppression des tests e2e lors de la fusion des fonctionnalités épiques [#3635](https://github.com/SocialGouv/egapro/issues/3635).
- **Orchestration :** Ajout d'outils de planification, de dimensionnement de sprint et de vélocité [#3644](https://github.com/SocialGouv/egapro/issues/3644).
- **Notifications :** Correction des URL des emails et refactorisation du système de templates [#3606](https://github.com/SocialGouv/egapro/issues/3606). Extraction du kit de templates React Email [#3561](https://github.com/SocialGouv/egapro/issues/3561).
- **Tests :** Ajout d'un agent tu-dev pour la création de tests unitaires et d'intégration [#3620](https://github.com/SocialGouv/egapro/issues/3620).
- **Lock parcours :** Mise en place d'un lock pour le parcours de conformité [#3556](https://github.com/SocialGouv/egapro/issues/3556) et [#3753](https://github.com/SocialGouv/egapro/issues/3753).

### Autres changements
- **Documentation :** Ajout d'un diagramme de flux du parcours CSE 2027 avec superposition des étapes FSM [#3433](https://github.com/SocialGouv/egapro/issues/3433).
- **Scripts :** Ajout d'un script `seed-demo-stats` pour tester les graphiques statistiques en local [#3569](https://github.com/SocialGouv/egapro/issues/3569).
- **Corrections visuelles :** Diverses corrections visuelles et alignements avec Figma dans le parcours de conformité et l'espace personnel [#3532](https://github.com/SocialGouv/egapro/issues/3532), [#3538](https://github.com/SocialGouv/egapro/issues/3538), [#3540](https://github.com/SocialGouv/egapro/issues/3540), [#3552](https://github.com/SocialGouv/egapro/issues/3552), [#3553](https://github.com/SocialGouv/egapro/issues/3553), [#3554](https://github.com/SocialGouv/egapro/issues/3554), [#3582](https://github.com/SocialGouv/egapro/issues/3582), [#3583](https://github.com/SocialGouv/egapro/issues/3583), [#3588](https://github.com/SocialGouv/egapro/issues/3588), [#3589](https://github.com/SocialGouv/egapro/issues/3589), [#3594](https://github.com/SocialGouv/egapro/issues/3594), [#3651](https://github.com/SocialGouv/egapro/issues/3651), [#3652](https://github.com/SocialGouv/egapro/issues/3652), [#3653](https://github.com/SocialGouv/egapro/issues/3653).
- **Correction de bugs :** Diverses corrections de bugs liés à la validation des champs, aux étiquettes manquantes et aux problèmes de copier-coller.
