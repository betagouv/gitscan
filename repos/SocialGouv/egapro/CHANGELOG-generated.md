## Changelog : egapro (30 derniers jours, au 2024-06-23)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de l'expérience utilisateur, notamment via des corrections d'alignement visuel et des améliorations du parcours de conformité. Des efforts importants ont également été déployés pour l'intégration d'outils d'analyse (Matomo) pour un suivi précis de l'utilisation de la plateforme, tout en respectant la conformité CNIL. Enfin, des améliorations techniques ont été apportées à l'infrastructure CI/CD et à l'orchestration des tests.

### Évolutions fonctionnelles
- Amélioration du parcours de conformité avec alignement visuel des formulaires "Évaluation conjointe" et "Téléchargement de fichiers" selon les maquettes Figma. [#3583](https://github.com/SocialGouv/egapro/issues/3583) [#3651](https://github.com/SocialGouv/egapro/issues/3651)
- Correction de l'affichage de la page de récapitulatif de la deuxième déclaration, masquant les éléments A-F et ajustant le titre et le bouton en fonction des conditions. [#3650](https://github.com/SocialGouv/egapro/issues/3650)
- Amélioration de l'alignement visuel de l'indicateur par catégorie dans le parcours de mise en conformité. [#3652](https://github.com/SocialGouv/egapro/issues/3652)
- Découplage de la lecture du brouillon de la date limite de la campagne. [#3594](https://github.com/SocialGouv/egapro/issues/3594) [#3656](https://github.com/SocialGouv/egapro/issues/3656)
- Refonte des pages d'avis du CSE. [#3639](https://github.com/SocialGouv/egapro/issues/3639)
- Intégration de l'historique des statuts des déclarations. [#3611](https://github.com/SocialGouv/egapro/issues/3611)
- Correction des URLs des emails et refactorisation du système de templates. [#3606](https://github.com/SocialGouv/egapro/issues/3606)
- Affichage du récapitulatif de la déclaration sur la page de détails de l'administration. [#3437](https://github.com/SocialGouv/egapro/issues/3437) [#3590](https://github.com/SocialGouv/egapro/issues/3590)
- Ajout d'un diagramme de flux du parcours CSE 2027 avec superposition des étapes FSM. [#3433](https://github.com/SocialGouv/egapro/issues/3433)
- Ajout de nouveaux indicateurs de suivi Matomo pour le modèle et les liens d'aide. [#3707](https://github.com/SocialGouv/egapro/issues/3707)
- Implémentation de la conformité CNIL pour Matomo (exemption de consentement). [#3655](https://github.com/SocialGouv/egapro/issues/3655)
- Ajout de graphes Matomo sur la page /admin/stats (usage du modèle, liens d'aide, répartition par appareil). [#3658](https://github.com/SocialGouv/egapro/issues/3658)
- Préservation de l'URL cible lors de la redirection après la connexion. [#3718](https://github.com/SocialGouv/egapro/issues/3718)

### Évolutions techniques
- Ajout d'un agent e2e-dev en fin de pipeline pour les tests. [#3654](https://github.com/SocialGouv/egapro/issues/3654)
- Ajout d'une vérification du journal monotone pour éviter l'omission silencieuse des migrations. [#3557](https://github.com/SocialGouv/egapro/issues/3557) [#3560](https://github.com/SocialGouv/egapro/issues/3560)
- Ajout d'outils de planification, de dimensionnement de sprint et de vélocité. [#3644](https://github.com/SocialGouv/egapro/issues/3644)
- Ajout d'un agent tu-dev pour la création de tests unitaires et d'intégration. [#3620](https://github.com/SocialGouv/egapro/issues/3620)
- Suppression des tests e2e lors de la fusion des fonctionnalités épiques. [#3635](https://github.com/SocialGouv/egapro/issues/3635)
- Refactorisation du système de templates d'emails avec extraction d'un kit React Email. [#3561](https://github.com/SocialGouv/egapro/issues/3561)
- Implémentation du versioning des CGU. [#2626](https://github.com/SocialGouv/egapro/issues/2626)

### Autres changements
- Attribution de noms de fichiers générés. [#3643](https://github.com/SocialGouv/egapro/issues/3643)
- Ajout de statistiques K5 (taux d'abandon par étape) et K19 (entonnoir de complétion). [#3218](https://github.com/SocialGouv/egapro/issues/3218) [#3546](https://github.com/SocialGouv/egapro/issues/3546) et [#3222](https://github.com/SocialGouv/egapro/issues/3222) [#3545](https://github.com/SocialGouv/egapro/issues/3545)
- Ajout de statistiques K7 (distribution des scores publics). [#3551](https://github.com/SocialGouv/egapro/issues/3551)
- Correction de problèmes d'installation de Playwright. [#3591](https://github.com/SocialGouv/egapro/issues/3591)
- Ajout d'un système de cache avec sauvegarde en base de données. [#3537](https://github.com/SocialGouv/egapro/issues/3537)
- Désactivation de l'autocomplétion du navigateur sur tous les formulaires. [#3539](https://github.com/SocialGouv/egapro/issues/3539) [#3548](https://github.com/SocialGouv/egapro/issues/3548)
