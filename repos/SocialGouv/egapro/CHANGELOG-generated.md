## Changelog : egapro (30 derniers jours, au 2026-06-25)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau du parcours de conformité et de l'administration. Des efforts ont également été faits pour améliorer le suivi analytique et la performance de la plateforme, ainsi que pour renforcer la sécurité et la conformité.

### Évolutions fonctionnelles
- **Parcours de conformité :** Lecture seule du parcours de conformité pour certaines étapes [#3494](https://github.com/SocialGouv/egapro/issues/3494) [#3755].
- **Étapes de rémunération :** Correction des libellés des étapes de rémunération dans l'espace personnel [#3761].
- **Avis CSE :** Refonte complète des pages d'avis du CSE [#3476](https://github.com/SocialGouv/egapro/issues/3639).
- **Historique des statuts :** Intégration de l'historique des statuts dans l'application [#3584](https://github.com/SocialGouv/egapro/issues/3611).
- **Administration :** Affichage du récapitulatif de la déclaration sur la page de détail de l'administration [#3437](https://github.com/SocialGouv/egapro/issues/3590).
- **Authentification :** Préservation de l'URL cible lors de la redirection après la connexion [#3718].
- **Noms de fichiers :** Possibilité d'assigner des noms de fichiers générés [#3516](https://github.com/SocialGouv/egapro/issues/3643).
- **Statistiques Admin :** Ajout de comptages d'engagement CSE et du nombre d'utilisateurs par entreprise [#3756].

### Évolutions techniques
- **Analytics :** Implémentation de Matomo pour le suivi analytique, avec prise en compte de la conformité CNIL (exemption de consentement) [#3655]. Ajout d'événements Matomo pour le modèle indicateur 7 et les liens d'aide [#3707].
- **CI/CD :** Ajout d'un agent e2e-dev en fin de pipeline [#3654]. Ajout d'une vérification du journal monotone pour éviter les sauts de migration silencieux [#3557](https://github.com/SocialGouv/egapro/issues/3560).
- **Orchestration :** Amélioration des outils de planification, de dimensionnement de sprint et de vélocité [#3644].
- **Tests :** Correction d'un blocage de l'installation de Playwright dans les tests E2E [#3591].
- **Refactoring :** Découplage du statut "draft" de la date limite de la campagne [#3594](https://github.com/SocialGouv/egapro/issues/3656).
- **Scripts :** Ajout d'un script `seed-demo-stats` pour tester les graphiques de statistiques en local [#3569].

### Autres changements
- **Documentation :** Ajout d'un diagramme de flux du parcours CSE 2027 avec les étapes FSM superposées [#3433].
- **Notifications :** Correction des URLs des emails et refactorisation du système de templates [#3606].
- **Suppression de tests E2E :** Suppression des tests E2E lors de la fusion des fonctionnalités dans les épiques [#3635].
