# Synthèse d'activité : betagouv (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation betagouv est marquée par une forte concentration sur l'amélioration de la qualité des données, la correction de bugs et l'ajout de nouvelles fonctionnalités pour faciliter l'utilisation des différents services. Plusieurs dépôts ont bénéficié de mises à jour significatives, notamment concernant la gestion des subventions, l'aide aux jeunes, la cartographie des données, et les outils d'aide à la décision. L'accent est mis sur l'amélioration de l'expérience utilisateur, la sécurité et la conformité des applications. Plusieurs projets ont également bénéficié de l'intégration de nouveaux outils et technologies, comme l'OCR Mistral ou l'API RNVP.

## Sécurité
Plusieurs dépôts ont intégré des améliorations de sécurité :
- [api-subventions-asso](/repos/betagouv/api-subventions-asso) a renforcé la sécurité avec l'ajout d'un mécanisme de feedback utilisateur et l'implémentation d'un "cooldown" pour les mises à jour automatiques de dépendances.
- [depots-sauvages](/repos/betagouv/depots-sauvages) a intégré Sentry pour le monitoring et le suivi des erreurs.
- [gestion-des-subventions-locales](/repos/betagouv/gestion-des-subventions-locales) a ajouté l'authentification à deux facteurs (OTP) et une protection contre les attaques par force brute.
- [euphrosyne-digilab](/repos/betagouv/euphrosyne-digilab) a mis à jour ses dépendances pour améliorer la sécurité.
- [grist-cron-grist-to-brevo](/repos/betagouv/grist-cron-grist-to-brevo) a amélioré la validation des adresses email pour éviter l'envoi à des adresses invalides.

## Autres changements notables
Plusieurs évolutions techniques majeures ont été réalisées :
- [Resultats-Elections-FPT](/repos/betagouv/Resultats-Elections-FPT) a migré vers Vue.js et mis en place une CI/CD.
- [ComparIA](/repos/betagouv/ComparIA) a refactorisé le calcul des classements et implémenté un filtre anti-spam.
- [a-just](/repos/betagouv/a-just) a mis à jour l'extracteur de données pour la collecte 2026 et refactorisé l'architecture des tests E2E.
- [acces-cible](/repos/betagouv/acces-cible) a mis à niveau Ruby vers la version 4.0.1.
- [api-subventions-asso](/repos/betagouv/api-subventions-asso) a réalisé un refactoring majeur de l'architecture de l'API.
- [archeologia-pipeline](/repos/betagouv/archeologia-pipeline) a bénéficié d'une refonte majeure pour améliorer les performances avec le traitement parallèle et l'inférence ONNX.
- [dsfr-form-builder](/repos/betagouv/dsfr-form-builder) a ajouté un site de documentation et de démonstration.
- [fondation](/repos/betagouv/fondation) a ajouté la gestion des données LoLfi.

## Dépôts les plus actifs
- [Aidants_Connect](/repos/betagouv/Aidants_Connect) : Ajout de nouvelles fonctionnalités pour la gestion des aidants et des conseillers, ainsi que des corrections de bugs.
- [ComparIA](/repos/betagouv/ComparIA) : Ajout de nouveaux modèles de langage et amélioration de la réactivité.
- [a-just](/repos/betagouv/a-just) : Corrections et améliorations de l'interface et de l'extracteur de données.
- [api-subventions-asso](/repos/betagouv/api-subventions-asso) : Refactoring de l'architecture et ajout de nouvelles fonctionnalités pour la gestion des subventions.
- [acces-cible](/repos/betagouv/acces-cible) : Amélioration de la robustesse et ajout de nouvelles fonctionnalités pour la gestion des sites.
- [Resultats-Elections-FPT](/repos/betagouv/Resultats-Elections-FPT) : Migration vers Vue.js et mise en place d'une CI/CD.
- [euphrosyne](/repos/betagouv/euphrosyne) : Amélioration de l'interface utilisateur et intégration du Design System de la République Française (DSFR).
