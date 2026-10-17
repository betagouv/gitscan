# Synthèse d'activité : demarche-numerique (du 14/09 au 21/09)

## Résumé de l'activité
L'activité de cette période est marquée par une montée en puissance de l'automatisation et un renforcement de la sécurité des services. L'outil d'extraction de données [la_taupe](/repos/demarche-numerique/la_taupe) gagne significativement en précision et en capacité de traitement, tandis que la plateforme principale [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) améliore sa résilience face aux indisponibilités de services tiers et la protection de ses accès critiques.

Parallèlement, l'écosystème s'élargit avec l'initialisation de nouveaux projets structurants, notamment pour la documentation de la nouvelle version de la démarche et la création d'un espace d'échange dédié à la communauté.

## Sécurité
- Renforcement de la sécurité des comptes "Super Admin" via l'enrôlement OTP et le verrouillage automatique dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Implémentation d'un sandboxing pour le traitement des images (libvips) afin de sécuriser le serveur dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- **Optimisation de l'extraction de données :** Passage à un nouveau moteur OCR plus performant et ajout de fonctionnalités de traitement par lots (batch) pour [la_taupe](/repos/demarche-numerique/la_taupe).
- **Résilience et performance :** Introduction d'un mode "dégradé" pour la saisie des données d'entreprise en cas d'indisponibilité des API et migration vers Sidekiq 8 dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- **Flexibilité de stockage :** Ajout de la prise en charge des protocoles S3 et Swift ainsi qu'une simplification des dépendances pour [ds_proxy](/repos/demarche-numerique/ds_proxy).
- **Lancement de nouveaux projets :** Initialisation des dépôts pour la documentation de la version 2 ([doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr)) et pour l'espace de partage de l'écosystème ([commun.demarche.numerique.gouv.fr](/repos/demarche-numerique/commun.demarche.numerique.gouv.fr)).

## Dépôts les plus actifs
- [la_taupe](/repos/demarche-numerique/la_taupe) : Évolutions majeures de l'OCR, de la précision d'extraction des RIB et ajout du traitement par lots.
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Améliorations de la sécurité, de la résilience du service et des performances de recherche.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Extension des capacités de stockage et optimisation de l'infrastructure.
