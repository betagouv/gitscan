## Changelog : egapro (30 derniers jours, au 20 août 2026)

### Résumé
Cette période a été marquée par une phase intense de stabilisation et d'affinage de l'expérience utilisateur. Les efforts se sont concentrés sur la fiabilisation du tunnel de déclaration de rémunération, l'alignement rigoureux des interfaces sur les maquettes de design (Figma) et le renforcement de la couverture de tests automatisés pour garantir la qualité des parcours.

### Évolutions fonctionnelles
- **Déclaration de rémunération** : Fiabilisation des calculs (écarts, quartiles, période de référence), préparation de la campagne 2027 ([#4244](https://github.com/SocialGouv/egapro/issues/4244)) et sécurisation du tunnel en bloquant l'accès si les informations obligatoires (téléphone, CSE) sont manquantes ([#4117](https://github.com/SocialGouv/egapro/issues/4117)).
- **Mon espace & Profil** : Refonte visuelle conforme aux maquettes Figma (espacements, couleurs, typographie) et mise en place d'une nouvelle modale pour la gestion du profil ([#4188](https://github.com/SocialGouv/egapro/issues/4188)).
- **Parcours de conformité et CSE** : Correction de boucles de redirection infinie et optimisation du tunnel de dépôt d'avis CSE ([#4061](https://github.com/SocialGouv/egapro/issues/4061), [#4148](https://github.com/SocialGouv/egapro/issues/4148)).
- **Documents et Exports** : Amélioration de la qualité des exports PDF (gestion des titres et des en-têtes) et enrichissement des données exportées via l'API SUIT ([#4145](https://github.com/SocialGouv/egapro/issues/4145), [#3993](https://github.com/SocialGouv/egapro/issues/3993)).

### Évolutions techniques
- **Tests et Qualité** : Extension majeure de la couverture de tests de bout en bout (E2E) sur l'ensemble des parcours ([#4097](https://github.com/SocialGouv/egapro/issues/4097)) et ajustement des seuils de criticité dans la CI ([#4150](https://github.com/SocialGouv/egapro/issues/4150)).
- **CI/CD et Déploiement** : Automatisation du versioning des images pour les environnements de test, génération assistée par IA des changelogs et sécurisation des appels vers SUIT via certificat mTLS ([#4046](https://github.com/SocialGouv/egapro/issues/4046), [#4101](https://github.com/SocialGouv/egapro/issues/4101)).
- **Environnement de développement** : Optimisation de l'authentification des nouveaux environnements de travail et mise à jour des mocks pour les données GIP-MDS ([#4095](https://github.com/SocialGouv/egapro/issues/4095)).

### Autres changements
- Mise à jour de la documentation technique (nomenclature des tests) et de l'organisation des outils de suivi.
