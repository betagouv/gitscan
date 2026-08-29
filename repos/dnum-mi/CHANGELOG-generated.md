# Synthèse d'activité : dnum-mi (du 01/08 au 25/08/2026)

## Résumé de l'activité
L'activité de cette période est marquée par un renforcement massif de la sécurité et de l'automatisation des processus de déploiement au sein de l'organisation. L'usage des GitHub Apps a été généralisé pour sécuriser les accès et les publications, tandis que les capacités de gestion des conteneurs et des charts Helm ont été considérablement enrichies.

Parallèlement, des évolutions majeures ont été apportées aux produits pour améliorer l'expérience utilisateur et la conformité : mise en place de flux de gestion des conditions générales d'utilisation ([bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique)), intégration de moteurs de corrélation de données ([referentiel-applications](/repos/dnum-mi/referentiel-applications)) et actualisation du périmètre de surveillance des services de l'État ([dashlord](/repos/dnum-mi/dashlord)).

## Sécurité
- **Renforcement de l'authentification** : Migration massive vers l'utilisation de GitHub Apps pour sécuriser les workflows de publication et de scan ([test-helm](/repos/dnum-mi/test-helm), [test-app](/repos/dnum-mi/test-app), [fabnum-cicd](/repos/dnum-mi/fabnum-cicd)).
- **Sécurisation des pipelines** : Application du principe de moindre privilège, protection contre les injections de commandes et ajout de scans de secrets via Gitleaks ([test-helm](/repos/dnum-mi/test-helm), [test-app](/repos/dnum-mi/test-app), [fabnum-cicd](/repos/dnum-mi/fabnum-cicd)).
- **Intégrité des composants** : Mise en place de l'attestation des images Docker (via Cosign/SBOM) et des charts Helm pour garantir la traçabilité ([fabnum-cicd](/repos/dnum-mi/fabnum-cicd)).
- **Corrections de vulnérabilités** : Résolution de failles de type XSS et de vulnérabilités dans les modules ([referentiel-applications](/repos/dnum-mi/referentiel-applications), [ds-api-client](/repos/dnum-mi/ds-api-client)).
- **Administration** : Amélioration des contrôles de sécurité pour les administrateurs, incluant la gestion du bannissement et la sécurisation de l'impersonation ([referentiel-applications](/repos/dnum-mi/referentiel-applications)).

## Autres changements notables
- **Évolutions produits et UX** : Implémentation d'un système complet d'acceptation des CGU ([bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique)), d'un moteur de détection de corrélations avec scoring ([referentiel-applications](/repos/dnum-mi/referentiel-applications)) et amélioration du rendu des icônes pour les environnements hors-ligne et SSR ([vue-dsfr](/repos/dnum-mi/vue-dsfr)).
- **Infrastructure et CI/CD** : Migrations techniques importantes (NestJS 11, Node 24, pnpm) et optimisation de l'automatisation des releases, du nettoyage des caches et de la gestion des monorepos ([referentiel-applications](/repos/dnum-mi/referentiel-applications), [vue-dsfr](/repos/dnum-mi/vue-dsfr), [test-app](/repos/dnum-mi/test-app), [fabnum-cicd](/repos/dnum-mi/fabnum-cicd)).
- **Monitoring** : Mise à jour massive des listes d'URLs surveillées pour assurer la continuité du monitoring des services publics et des préfectures ([dashlord](/repos/dnum-mi/dashlord), [dashlord-extended](/repos/dnum-mi/dashlord-extended)).
- **IA et Développement** : Enrichissement de la documentation pour l'intégration d'agents d'IA et activation des serveurs LSP pour améliorer l'expérience de développement ([starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode), [vue-dsfr](/repos/dnum-mi/vue-dsfr)).

## Dépôts les plus actifs
- [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) : Montée en puissance de la sécurité et de l'automatisation des publications (Helm, Docker, NPM).
- [referentiel-applications](/repos/dnum-mi/referentiel-applications) : Évolutions majeures de fonctionnalités (corrélations) et migration technique (NestJS).
- [vue-dsfr](/repos/dnum-mi/vue-dsfr) : Amélioration de la gestion des icônes et stabilisation de l'infrastructure de build.
- [test-app](/repos/dnum-mi/test-app) : Passage en version 1.0.0 et optimisation des pipelines CI/CD.
- [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) : Implémentation du flux de conformité légale (CGU).
