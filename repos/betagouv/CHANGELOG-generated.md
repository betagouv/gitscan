# Synthèse d'activité : betagouv (derniers 7 jours)

## Résumé de l'activité
L'organisation betagouv a connu une semaine riche en activités, avec des mises à jour significatives sur de nombreux dépôts. Plusieurs projets ont bénéficié d'améliorations de l'interface utilisateur et de l'expérience utilisateur, notamment *diagbruit.beta.gouv.fr*, *espace-membre-next* et *france-chaleur-urbaine*.  Des efforts importants ont été consacrés à l'amélioration de la qualité du code, à la correction de bugs et à l'ajout de nouvelles fonctionnalités, comme l'intégration de l'OCR Mistral dans *document-ia* ou la gestion des CPOM dans *bhasile*.  La sécurité a également été une priorité, avec des mises à jour de dépendances et l'ajout de systèmes de surveillance comme Sentry dans *depots-sauvages*.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de dépendances pour corriger des vulnérabilités de sécurité, notamment *dsfr-assets*, *dsfr-form-builder*, *euphrosyne-tools-api* et *depots-sauvages*. L'intégration de Sentry dans *depots-sauvages* permet également une meilleure surveillance des erreurs et une réaction plus rapide aux incidents de sécurité.

## Autres changements notables
*   *ComparIA* a subi une refonte majeure de son architecture backend, passant à FastAPI et Pydantic pour une meilleure performance.
*   *a-just* a vu des améliorations significatives de son extracteur de données pour la collecte 2026.
*   *api-subventions-asso* a vu une refonte de son interface `port` et une amélioration de la gestion des erreurs.
*   *archeologia-pipeline* a bénéficié d'une refonte majeure pour améliorer ses performances grâce à l'utilisation du traitement parallèle et de l'inférence ONNX.
*   *doc.incubateur.net-communaute* a connu une restructuration complète de sa documentation.

## Dépôts les plus actifs
*   **aides-jeunes**: Amélioration de l'expérience utilisateur avec l'ajout de nouveaux accompagnements personnalisés et la simplification du formulaire de contribution.
*   **api-engagement**: Ajout de nouvelles fonctionnalités pour la gestion des campagnes et des missions, ainsi que des améliorations de l'interface de modération.
*   **diagbruit.beta.gouv.fr**: Amélioration de l'interface utilisateur, ajout de pages légales et gestion des polygones de sources de bruit.
*   **depots-sauvages**: Corrections de bugs, amélioration de la gestion des erreurs et ajout d'un système de surveillance avec Sentry.
*   **document-ia**: Ajout de la prise en charge de l'OCR Mistral avec des images et amélioration de la gestion des schémas complexes.
*   **euphrosyne**: Intégration progressive du Design System de la République Française (DSFR) et correction de bugs graphiques.
*   **france-chaleur-urbaine**: Amélioration de l'expérience utilisateur sur la page de simulation et le formulaire de contact, ainsi que des mises à jour des données réseaux de chaleur.
*   **espace-membre-next**: Amélioration de la gestion des membres, de l'activation et de la vérification des comptes.
*   **bhasile**: Ajout de la gestion des CPOM et amélioration de l'interface utilisateur.
*   **dsfr-form-builder**: Corrections de bugs, amélioration de la gestion des champs de formulaire et ajout d'une documentation et d'un site de démonstration.
